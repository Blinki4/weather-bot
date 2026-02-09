from api.yandex import get_weather_novo, get_weather_krd
from utils.format_response import format_response


def send_novo_weather(chat_id, bot):
    weather_novo = get_weather_novo()
    bot.send_message(
        chat_id,
        text=format_response(weather_novo, 'novo')
    )

def send_krd_weather(chat_id, bot):
    weather_novo = get_weather_krd()
    bot.send_message(
        chat_id,
        text=format_response(weather_novo, 'krd')
    )