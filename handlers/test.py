from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards import admin_builders
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
        reply_markup=admin_builders.admission_year_kb(),
    )


@router.callback_query(GroupCreation.admission_year)
async def group_admission_year(query: CallbackQuery, state: FSMContext):

    await state.update_data(admission_year=query.data)
