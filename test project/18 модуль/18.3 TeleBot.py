# audio — аудиозапись;
# photo — фотография, картинка;
# voice — голосовое сообщение;
# video — видеозапись;
# document — документ;
# text — текстовое сообщение;
# location — геолокация;
# contact — контакт;
# sticker — стикер.

import telebot

# TOKEN = "5648658809:AAHCuIKWV6PcHj9zCc0GdU3lFEcHDGH3xV4"

bot = telebot.TeleBot("5648658809:AAHCuIKWV6PcHj9zCc0GdU3lFEcHDGH3xV4")



# # filters — фильтры, определяющие, следует ли вызывать декорированную функцию для соответствующего сообщения или нет. У одного обработчика может быть несколько фильтров.
# @bot.message_handler(filters)
# def function_name(message):
#     bot.reply_to(message, "This is a message handler")


# # Обрабатываются все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass
# Возвращает сообщения
# @bot.message_handler()
# def repeat(message):
#     bot.send_message(message.chat.id, message.text)

# Ответ на сообщения
@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f'Приветствую, {message.chat.username}')

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")

# Ответ на фотографию
@bot.message_handler(content_types=['photo'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f"<b>«Nice meme XDD»{message.chat.username} {message.from_user.first_name} "
                          f"{message.from_user.last_name}</b>",
                 parse_mode='html')
bot.polling(none_stop=True) #говорит, что бот должен стараться не прекращать работу при возникновении каких-либо ошибок.