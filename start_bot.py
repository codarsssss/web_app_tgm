from aiogram.types import InlineKeyboardButton, KeyboardButton, WebAppInfo, ReplyKeyboardMarkup
from aiogram import types
from aiogram import Dispatcher, Bot

from secret import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def init_func(message: types.Message):
    web_app_info = types.WebAppInfo(url="https://demo.pixlpark.ru/printing/hardcover-photobooks-templates/for-20x20-hard?ws=11819a1630fb09355d289f9fab3e335c&p=11&q=1&oq=0", display_text="Открыть страницу выбора..")
    button = types.InlineKeyboardButton(text="открыть то что нужно", web_app=web_app_info)
    keyboard = types.InlineKeyboardMarkup().add(button)
    await bot.send_message(message.from_user.id, 'Тест', reply_markup=keyboard)


if __name__ == '__main__':
    dp.start_polling(dp, skip_updates=True)
