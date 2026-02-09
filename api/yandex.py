import requests
from dto.weather import Weather

access_key = '7f7c2438-9dc3-4219-9de6-2fdcdd783aed'

def get_weather_krd():
    headers = {
        'X-Yandex-Weather-Key': access_key
    }

    response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=45.03277&lon=38.97694', headers=headers)
    data = response.json()
    return {
        'now': {
            'temp': data['fact']['temp'],
            'feels_like': data['fact']['feels_like']
        },
        'today': {
            'date': data['forecasts'][0]['date'],
            'morning': {
                'average': data['forecasts'][0]['parts']['morning']['temp_avg'],
                'feels_like': data['forecasts'][0]['parts']['morning']['feels_like']
            },
            'evening': {
                'average': data['forecasts'][0]['parts']['evening']['temp_avg'],
                'feels_like': data['forecasts'][0]['parts']['evening']['feels_like']
            }
        },
        'tomorrow': {
            'date': data['forecasts'][1]['date'],
            'morning': {
                'average': data['forecasts'][1]['parts']['morning']['temp_avg'],
                'feels_like': data['forecasts'][1]['parts']['morning']['feels_like']
            },
            'evening': {
                'average': data['forecasts'][1]['parts']['evening']['temp_avg'],
                'feels_like': data['forecasts'][1]['parts']['evening']['feels_like']
            }
        },
        'after_tomorrow': {
            'date': data['forecasts'][2]['date'],
            'morning': {
                'average': data['forecasts'][2]['parts']['morning']['temp_avg'],
                'feels_like': data['forecasts'][2]['parts']['morning']['feels_like']
            },
            'evening': {
                'average': data['forecasts'][2]['parts']['evening']['temp_avg'],
                'feels_like': data['forecasts'][2]['parts']['evening']['feels_like']
            }
        }
    }


def get_weather_novo():
    headers = {
        'X-Yandex-Weather-Key': access_key
    }

    response = requests.get('https://api.weather.yandex.ru/v2/forecast?lat=44.7167&lon=37.7667&limit=3', headers=headers)
    data = response.json()
    return {
        'now': {
            'temp': data['fact']['temp'],
            'feels_like': data['fact']['feels_like']
        },
        'today': {
            'date': data['forecasts'][0]['date'],
            'morning': {
                'average': data['forecasts'][0]['parts']['morning']['temp_avg'],
                'feels_like': data['forecasts'][0]['parts']['morning']['feels_like']
            },
            'evening': {
                'average': data['forecasts'][0]['parts']['evening']['temp_avg'],
                'feels_like': data['forecasts'][0]['parts']['evening']['feels_like']
            }
        },
        'tomorrow': {
            'date': data['forecasts'][1]['date'],
            'morning': {
                'average': data['forecasts'][1]['parts']['morning']['temp_avg'],
                'feels_like': data['forecasts'][1]['parts']['morning']['feels_like']
            },
            'evening': {
                'average': data['forecasts'][1]['parts']['evening']['temp_avg'],
                'feels_like': data['forecasts'][1]['parts']['evening']['feels_like']
            }
        },
        'after_tomorrow': {
            'date': data['forecasts'][2]['date'],
            'morning': {
                'average': data['forecasts'][2]['parts']['morning']['temp_avg'],
                'feels_like': data['forecasts'][2]['parts']['morning']['feels_like']
            },
            'evening': {
                'average': data['forecasts'][2]['parts']['evening']['temp_avg'],
                'feels_like': data['forecasts'][2]['parts']['evening']['feels_like']
            }
        }
    }