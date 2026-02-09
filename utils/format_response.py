def format_response(data, city):
    title = ''
    if city == 'novo':
        title = 'НОВОРОССИЙСК'
    elif city == 'krd':
        title = 'КРАСНОДАР'
    return f"""
   **{title}**
🌡 **ТЕКУЩАЯ ПОГОДА**
├ Температура: {data['now']['temp']}°C
└ Ощущается как: {data['now']['feels_like']}°C
────────────────────
📅 **СЕГОДНЯ**
├ Утро 🛏️
│   ├ Фактически: {data['today']['morning']['average']}°C
│   └ Ощущается: {data['today']['morning']['feels_like']}°C
└ Вечер 🌆
    ├ Фактически: {data['today']['evening']['average']}°C
    └ Ощущается: {data['today']['evening']['feels_like']}°C
────────────────────
📅 **ЗАВТРА**
├ Утро 🌅
│   ├ Фактически: {data['tomorrow']['morning']['average']}°C
│   └ Ощущается: {data['tomorrow']['morning']['feels_like']}°C
└ Вечер 🌃
    ├ Фактически: {data['tomorrow']['evening']['average']}°C
    └ Ощущается: {data['tomorrow']['evening']['feels_like']}°C
────────────────────
📅 **ПОСЛЕЗАВТРА**
├ Утро 🌄
│   ├ Фактически: {data['after_tomorrow']['morning']['average']}°C
│   └ Ощущается: {data['after_tomorrow']['morning']['feels_like']}°C
└ Вечер 🌇
    ├ Фактически: {data['after_tomorrow']['evening']['average']}°C
    └ Ощущается: {data['after_tomorrow']['evening']['feels_like']}°C
"""


if __name__ == '__main__':
    pass