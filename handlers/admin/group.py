from datetime import datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from db.repository import GroupRepository
from db.session import SessionLocal
from keyboards import admin_builders, inline
from states import GroupCreation

router = Router()


@router.message(F.text == "GROUP")
async def create_group(message: Message, state: FSMContext):

    await message.answer("Введите название новой группы")
    await state.set_state(GroupCreation.name)


@router.message(GroupCreation.name)
async def group_name(message: Message, state: FSMContext):

    await state.update_data(name=message.text)
    await message.answer("введите уникальный индентификатор группы")
    await state.set_state(GroupCreation.slug)


@router.message(GroupCreation.slug)
async def group_slug(message: Message, state: FSMContext):

    await state.update_data(slug=message.text)
    await message.answer(
        "выберете год поступления",
        reply_markup=admin_builders.admission_year_kb(datetime.now().year),
    )
    await state.set_state(GroupCreation.admission_year)


@router.callback_query(GroupCreation.admission_year)
async def group_admission_year(query: CallbackQuery, state: FSMContext):

    await state.update_data(admission_year=query.data)
    await state.set_state(GroupCreation.confirming)

    data = await state.get_data()

    await query.message.answer(
        f"""проверьте и подтвердите данные группы

Название - *{data["name"]}*
уникальный индентификатор - *{data["slug"]}*
год поступления - *{data["admission_year"]}*""",
        parse_mode="Markdown",
        reply_markup=inline.confirmation_kb,
    )

    await state.set_state(GroupCreation.confirming)


@router.callback_query(GroupCreation.confirming)
async def group_confirmation(query: CallbackQuery, state: FSMContext):

    data = await state.get_data()
    async with SessionLocal() as session:
        repo = GroupRepository(session)

        await repo.create(
            admission_year=datetime.strptime(f"{data['admission_year']}0109", "%Y%m%d"),
            name=data["name"],
            slug=data["slug"],
        )

    await query.message.answer("группа успешно зарегистрирована")
    await state.clear()
