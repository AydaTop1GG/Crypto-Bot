import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token
import handlers as h


# Установка уровня логов для отладки
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Все нужные переменные объявляются здесь
wallet_guide = "⏱Займёт не больше 5 минут\n\n\
    🔸*Binance* - Сайт Binance ==> Управление API ==> Создать API ==> Сгенерированный системой ==> ... потом допишу \n\
        🎮Далее, напишите данному боту */bncwallet* _Ваш API Ключ_\n\n\
    🔹*Yobit* - Сайт Yobit ==> Меню профиля ==> API Ключи ==> info & trade & deposits & withdrawals ==> \
    Создать новый ключ ==> Активируйте ключ ==> Скопировать Ключ \n\
        🎮Осталось написать данному боту */yobtwallet* _Ваш API Ключ_"
        
binance_wallet = "Не авторизированно❌"
yobit_wallet = "Не авторизированно❌"
main_info = "Здесь будет отображаться инфа, которую пользователь видит в первую очередь"
wallet_info = f"Binance: {binance_wallet}\nYobit: {yobit_wallet}\n\nЧтобы авторизировать кошелёк используйте команду /wallet"




############################


#from aiogram import Bot, Dispatcher, executor, types
#from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from aiogram.utils.callback_data import CallbackData

#import config


# dun_w это префикс, его можно ловить и стандартным text_startswith=...
#cd_walk = CallbackData("dun_w", "action", "floor")


#@dp.message_handler(commands=['start'])
#async def start(message: types.Message):
    
#    markup = InlineKeyboardMarkup(row_width=2).add(
#        InlineKeyboardButton(f"Налево",
#                             callback_data=cd_walk.new(
#                                 action='1',
#                                 floor=2
#                             )),
#        InlineKeyboardButton(f"Направо",
#                             callback_data=cd_walk.new(
#                                 action='2',
#                                 floor=2
#                             ))
#    )
#    await message.answer("text", reply_markup=markup)
#
#
#@dp.callback_query_handler(cd_walk.filter())
#async def button_press(call: types.CallbackQuery, callback_data: dict):
#    action = callback_data.get('action')  # 1 or 2
#    floor = callback_data.get('floor')  # 2



#####################





# Ловим сигналы callback_data от инлайн кнопок
@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    
    code = callback_query.data   # callback_data которая прилетает
    
    if code == 'Flow':
        await bot.answer_callback_query(callback_query.id, # Если ответ не будет долго возвращаться
            text='Простите, время ожидания превышено! Повторите операцию или обратитесь в тех поддержку.')
    
    elif code == 'Wallet':

        await callback_query.message.edit_text(wallet_info, reply_markup=h.wallet_menu)
        #await bot.answer_callback_query(callback_query.id,text='Простите, время ожидания превышено! Повторите операцию или обратитесь в тех поддержку.')
    
    elif code == 'Questions':
        await bot.answer_callback_query(callback_query.id,
            text='Простите, время ожидания превышено! Повторите операцию или обратитесь в тех поддержку.')
    
    elif code == 'back':
        #await bot.answer_callback_query(callback_query.id,text='Простите, время ожидания превышено! Повторите операцию или обратитесь в тех поддержку.')
        #await bot.send_message(message.from_user.id, main_info, reply_markup=h.main_menu)
        await callback_query.message.edit_text(main_info, reply_markup=h.main_menu)
       

    else:
        await bot.answer_callback_query(callback_query.id)
    
    #await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')



# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    
    # Отправка приветственного сообщения
    await bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAEFNLBixZumUmBmcAT3H2SmnCrPGRMyXAACaRcAAqnJOUoBu84B21ly6ikE')
    await message.answer("Привет! Я заряженный бот!")

    # Отправка кнопки пользователю
    await bot.send_message(message.from_user.id, main_info, reply_markup=h.main_menu)


@dp.message_handler(commands=['wallet'])
async def wallet_command(message: types.Message):

    await bot.send_message(message.from_user.id, wallet_guide, reply_markup=h.wallet_menu, parse_mode="Markdown")


# Привязка кошелька Binance
@dp.message_handler(commands=['bncwallet'])
async def wallet_command(message: types.Message):

    await bot.send_message(message.from_user.id, wallet_guide, reply_markup=h.wallet_menu, parse_mode="Markdown")


# Привязка кошелька Yobit
@dp.message_handler(commands=['yobtwallet'])
async def wallet_command(message: types.Message):

    await bot.send_message(message.from_user.id, wallet_guide, reply_markup=h.wallet_menu, parse_mode="Markdown")





# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)