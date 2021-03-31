import telebot
import gettingDataByNumber
import config

token = config.API_TOKEN
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name) + ',' + '\n' +
                 'чтоб узнать данные регистрации авто, укажите номер автомобиля.')


@bot.message_handler(content_types=['text'])
def test(message):
    number = message.text
    try:
        track_details = gettingDataByNumber.parseNumber(message.text)
        bot.send_message(message.chat.id, track_details)
    except:
        bot.send_message(message.chat.id, "Номер " + number + " не найден")

bot.polling()
