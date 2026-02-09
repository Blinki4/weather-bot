#TODO переписать на датаклассы

class WeatherNow:
    def __init__(
            self,
            temp: int,
            feels_like: int
    ):
        self.temp = temp
        self.feels_like = feels_like


class WeatherData:
    def __init__(
            self,
            average: int,
            feels_like: int
    ):
        self.average = average
        self.feels_like = feels_like


class WeatherDay:
    def __init__(
            self,
            date: str,
            morning: WeatherData,
            evening: WeatherData
    ):
        self.date = date
        self.morning = morning
        self.evening = evening



class Weather:
    def __init__(
            self,
            now: WeatherNow,
            today: WeatherDay,
            tomorrow: WeatherDay,
            after_tomorrow: WeatherDay
    ):
        self.now = now
        self.today = today
        self.tomorrow = tomorrow
        self.after_tomorrow = after_tomorrow


    def __str__(self):
        return f'{self.now}\n{self.today}\n{self.tomorrow}\n{self.after_tomorrow}\n'