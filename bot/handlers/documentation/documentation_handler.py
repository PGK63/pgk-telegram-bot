import os

from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData

documentation_type_callback = CallbackData('documentation_type_callback', 'type')
documentation_journal_type_callback = CallbackData('documentation_journal_type_callback', 'type')


async def documentation_handler(message: types.Message):
    await message.answer("Выберите категорию", reply_markup=types.InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text='Профиль',
                    callback_data=documentation_type_callback.new(type='profile')
                ),
                types.InlineKeyboardButton(
                    text='Журнал',
                    callback_data=documentation_type_callback.new(type='journal')
                )
            ],
            [
                types.InlineKeyboardButton(
                    text='Рапортичка',
                    callback_data=documentation_type_callback.new(type='raportichka')
                ),
                types.InlineKeyboardButton(
                    text='Группа',
                    callback_data=documentation_type_callback.new(type='group')
                )
            ],
            [
                types.InlineKeyboardButton(
                    text='Руководство',
                    callback_data=documentation_type_callback.new(type='guide')
                ),
                types.InlineKeyboardButton(
                    text='Отделения',
                    callback_data=documentation_type_callback.new(type='department')
                )
            ],
            [
                types.InlineKeyboardButton(
                    text='Специальности',
                    callback_data=documentation_type_callback.new(type='raportichka')
                ),
                types.InlineKeyboardButton(
                    text='Прдметы',
                    callback_data=documentation_type_callback.new(type='subject')
                )
            ],
            [
                types.InlineKeyboardButton(
                    text='Настройки',
                    callback_data=documentation_type_callback.new(type='settings')
                )
            ]
        ]
    ))


async def documentation_callback_handler(call: types.CallbackQuery, callback_data: dict):
    type = callback_data.get("type")

    if type == 'journal':
        await documentation_journal_handler(call)


async def documentation_journal_handler(call: types.CallbackQuery):
    await call.message.answer("Выберите что вы хотите", reply_markup=types.InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text='Создать журнал',
                    callback_data=documentation_journal_type_callback.new(type='create_journal')
                ),
                types.InlineKeyboardButton(
                    text='Поставить оценку',
                    callback_data=documentation_journal_type_callback.new(type='create_journal_column')
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text='Добавить тему',
                    callback_data=documentation_journal_type_callback.new(type='create_journal_topic')
                ),
            ]
        ]
    ))


async def documentation_journal_callback_handler(call: types.CallbackQuery, callback_data: dict):
    type = callback_data.get("type")
    doc_journal = os.path.join('resources', 'documentation', 'journal')

    if type == 'create_journal':
        await call.message.answer('Отправка видео')
        await call.message.answer_video(open(os.path.join(doc_journal, 'create_journal.mp4'), 'rb'))
    elif type == 'create_journal_topic':
        await call.message.answer('Отправка видео')
        await call.message.answer_video(open(os.path.join(doc_journal, 'create_journal_topic.mp4'), 'rb'))
    elif type == 'create_journal_column':
        await call.message.answer('Отправка видео')
        await call.message.answer_video(open(os.path.join(doc_journal, 'create_journal_column.mp4'), 'rb'))


def register_documentation(dp: Dispatcher):
    dp.register_message_handler(documentation_handler, commands=['documentation'])
    dp.register_callback_query_handler(documentation_callback_handler, documentation_type_callback.filter())
    dp.register_callback_query_handler(documentation_journal_callback_handler, documentation_journal_type_callback.filter())
