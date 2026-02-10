import telebot
from telebot import types
from api.rp_five_parser import RpFiveParser
from utils.handlers import send_novo_weather, send_krd_weather
from utils.setup_env import setup_env


def main():
    env = setup_env()
    bot = telebot.TeleBot(env[0])
    parser = RpFiveParser()



    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_krd = types.KeyboardButton('Краснодар (Яндекс)')
        btn_novo = types.KeyboardButton('Новороссийск (Яндекс)')
        btn_krd_rp_five = types.KeyboardButton('Краснодар (rp5)')
        btn_novo_rp_five = types.KeyboardButton('Новороссийск (rp5)')
        markup.add(btn_krd, btn_novo, btn_krd_rp_five, btn_novo_rp_five)
        bot.send_message(message.from_user.id, text='Че надо?', reply_markup=markup)



    # from_user видимо идентифицирует пользователя, чтобы бот отправлял ответ ему
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == '/help':
            bot.send_message(message.from_user.id, 'Напиши кто такой создатель...')
        elif message.text == 'Краснодар (Яндекс)':
            send_krd_weather(message.from_user.id, bot)
        elif message.text == 'Новороссийск (Яндекс)':
            send_novo_weather(message.from_user.id, bot)
        elif message.text == 'Краснодар (rp5)':
            parser.make_screenshot_krd()
            with open('today-weather-krd.png', 'rb') as photo:
                bot.send_photo(message.from_user.id, photo, caption='Лови!')
        elif message.text == 'Новороссийск (rp5)':
            parser.make_screenshot_novo()
            with open('today-weather-novo.png', 'rb') as photo:
                bot.send_photo(message.from_user.id, photo, caption='Лови!')
        elif message.text == 'Человек-паук':
            bot.send_message(message.from_user.id, 'Это создатель')
        else:
            bot.send_message(message.from_user.id, 'Пососи :(\n /start')

    bot.infinity_polling()

if __name__ == '__main__':
    main()