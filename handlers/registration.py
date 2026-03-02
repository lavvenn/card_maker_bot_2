from pathlib import Path

from aiogram import Bot, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from db.repository import PassRepository
from db.session import SessionLocal
from image_editor.pass_generator import PassGenirator
from keyboards.builders import goroup_kb_builder
from keyboards.inline import confirmation_kb
from keyboards.reply import main_kb
from states import Registration

router = Router()


@router.message(F.text == "📋Отправить данные")
async def start_registration(message: Message, state: FSMContext):
    await state.set_state(Registration.lastname)
    await message.answer(
        "Вы можите отменить отправку данных нажав на кнопку ❌Отмена",
    )
    await message.answer("Введите свою фамилию")


@router.message(Registration.lastname)
async def lastname_registration(message: Message, state: FSMContext):
    await state.update_data(lastname=message.text)
    await message.answer("Введите своё Имя")
    await state.set_state(Registration.firstname)


@router.message(Registration.firstname)
async def firstname_registration(message: Message, state: FSMContext):
    await state.update_data(firstname=message.text)
    await state.set_state(Registration.group)
    await message.answer("Выберете свою группу", reply_markup=goroup_kb_builder())


@router.callback_query(Registration.group)
async def group_registration(query: CallbackQuery, state: FSMContext):
    await state.update_data(group=query.data)
    await state.set_state(Registration.photo)

    await query.answer("")
    await query.message.answer("отправьте фото")
    await query.message.answer(
        "❗️перед отправкой обрежте фото так чтобы ваше лицо находилось в центре❗️",
    )


@router.message(Registration.photo)
async def photo_registration(message: Message, state: FSMContext):
    if message.photo:

        await state.update_data(photo=message.photo[-1].file_id)

        data = await state.get_data()

        await state.set_state(Registration.confirming)
        await message.answer_photo(
            photo=data["photo"],
            caption=f"""
❗️внимательно проверьте все данные перед подтверждением❗️
Фамилия: {data["lastname"]}
Имя: {data["firstname"]}

    Группа: {data["group"]}
    """,
            reply_markup=confirmation_kb,
        )

    else:
        await message.answer("Вы отправили не фото")


@router.callback_query(Registration.confirming)
async def confirmation_registration(query: CallbackQuery, state: FSMContext, bot: Bot):

    await query.answer("")

    genirator = PassGenirator()

    if query.data == "aprove":

        data = await state.get_data()

        photo_file = await bot.get_file(data["photo"])
        photo_path = f"tmp/{data['lastname']}_{data["firstname"]}.png"

        await bot.download_file(photo_file.file_path, photo_path)

        output_path = Path(
            f"result/{data["group"]}/{data['lastname']}_{data["firstname"]}.png",
        )

        async with SessionLocal() as session:
            repo = PassRepository(session)

            existing_pass = await repo.get_by_telegram_id(query.from_user.id)

            if existing_pass:
                await repo.update(
                    existing_pass,
                    lastname=data["lastname"],
                    firstname=data["firstname"],
                    group=data["group"],
                    photo_file_id=data["photo"],
                )
            else:
                await repo.create(
                    telegram_id=query.from_user.id,
                    lastname=data["lastname"],
                    firstname=data["firstname"],
                    group=data["group"],
                    photo_file_id=data["photo"],
                )

        genirator.genirate(
            data["firstname"],
            data["lastname"],
            photo_path,
            output_path,
        )

        await query.message.answer("WIP")

    else:
        await query.message.answer("Регистрация отменена", reply_markup=main_kb)
        await state.clear()
