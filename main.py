import telebot
from telebot import types
from api.rp_five_parser import RpFiveParser
from utils.setup_env import setup_env
import os
import http.server
import socketserver
import threading


def main():
    def start_http_server():
        class Handler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'OK')

        port = int(os.environ.get('PORT', 10000))
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"HTTP server started on port {port}")
            httpd.serve_forever()

    # Запускаем сервер в отдельном потоке
    server_thread = threading.Thread(target=start_http_server, daemon=True)
    server_thread.start()


    env = setup_env()
    bot = telebot.TeleBot(env[0])



    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # btn_krd = types.KeyboardButton('Краснодар (Яндекс)')
        # btn_novo = types.KeyboardButton('Новороссийск (Яндекс)')
        btn_krd_rp_five = types.KeyboardButton('Краснодар (rp5)')
        btn_novo_rp_five = types.KeyboardButton('Новороссийск (rp5)')
        markup.add(btn_krd_rp_five, btn_novo_rp_five)
        bot.send_message(message.from_user.id, text='Че надо?', reply_markup=markup)



    # from_user видимо идентифицирует пользователя, чтобы бот отправлял ответ ему
    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        print(message)
        if message.text == '/help':
            bot.send_message(message.from_user.id, 'Напиши кто такой создатель...')
        elif message.text == 'Краснодар (rp5)':
            parser = RpFiveParser()
            parser.make_screenshot_krd()
            with open('today-weather-krd.png', 'rb') as photo:
                bot.send_photo(message.from_user.id, photo, caption='Лови!')
        elif message.text == 'Новороссийск (rp5)':
            parser = RpFiveParser()
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