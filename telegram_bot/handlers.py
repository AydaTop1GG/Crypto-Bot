from aiogram import types



wallet_button = types.InlineKeyboardButton(text="🏦Wallet💳", callback_data='Wallet')

flow_button = types.InlineKeyboardButton(text="🦈Flow🌪", callback_data='Flow')

#questions_button = types.InlineKeyboardButton(text="Questions")

test1 = types.InlineKeyboardButton('Questions📞', url='https://t.me/CryptoBotTehSupport/7')


main_menu = types.InlineKeyboardMarkup().add(flow_button).row(wallet_button, test1)



back_button = types.InlineKeyboardButton(text="⬅️Вернуться", callback_data='back')

wallet_menu = types.InlineKeyboardMarkup().add(back_button)