import os

from aiogram import Dispatcher, types
from aiogram.utils.callback_data import CallbackData

from api.user.user_api import add_telegram_id

auth_type_callback = CallbackData('auth_type_callback', 'type')


async def auth_message_handler(message: types.Message):
    args = message.get_args()
    telegramId = message.from_user.id

    if args:
        response = add_telegram_id(telegramId, args)

        if response:
            await message.answer('Успешно')
        else:
            await message.answer('Ошибка')
    else:
        await message.answer(
            text="Выберите способ для регестриции",
            reply_markup=types.InlineKeyboardMarkup(
                row_width=1,
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(
                            text='Android 📱',
                            callback_data=auth_type_callback.new(type='android')
                        ),
                        types.InlineKeyboardButton(
                            text='Сайт 🌐',
                            callback_data=auth_type_callback.new(type='web')
                        )
                    ]
                ]
            )
        )


async def documentation_auth(call: types.CallbackQuery, callback_data: dict):
    type = callback_data.get("type")

    if type == 'android':
        # androidApk = os.path.join('resources', 'android', 'app_debug.apk')
        doc_auth = os.path.join('resources', 'documentation', 'auth')

        # await call.message.answer_document(open(androidApk, 'rb'))
        await call.message.answer('Отправка видео')
        await call.message.answer_video(
            open(os.path.join(doc_auth, 'telegram_auth.mp4'), 'rb'),
        )
    elif type == 'web':
        await call.message.answer("web")


def register_auth(dp: Dispatcher):
    dp.register_message_handler(auth_message_handler, commands=['start'])
    dp.register_callback_query_handler(documentation_auth, auth_type_callback.filter())
