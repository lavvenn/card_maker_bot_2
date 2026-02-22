from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.builders import goroup_kb_builder
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
    await message.answer("Выберете свою группу", reply_markup=goroup_kb_builder())
