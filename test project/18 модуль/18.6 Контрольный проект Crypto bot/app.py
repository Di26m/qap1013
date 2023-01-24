import telebot
from config import TOKEN, keys
from extensions import ConverthionExeption, CryptoConverter
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = f'Приветствую {message.chat.username}, чтобы начать работу, введите команду боту в следующем формате:\n ' \
           f'<имя валюты цену которой вы хотите узнать> <имя валюты в которой надо узнать цену первой валюты> ' \
           f'<количество первой валюты>\n Увидеть список доступных валют: /values \n Пример: доллар рубль 32'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def get_values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConverthionExeption("Слишком много или мало параметров. Должно быть 3")

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConverthionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        # total = round(abs(float(amount)) * float(total_base),4)
        text = f'Цена {amount} {quote} в {base} - <strong><u>{total_base}</u></strong>'
        bot.send_message(message.chat.id, text, parse_mode='html')


bot.polling(none_stop=True)
