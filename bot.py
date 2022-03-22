import telebot

bot = telebot.TeleBot('5138135947:AAEFtZ_Y-9d6xkDUJP2113ZvHjFX3tN0Tx8')

@bot.message_handler(commands=['start'])
def info(message):
    bot.send_message(message.chat.id, 'Это мой бот!')

bot.polling(none_stop=True)
