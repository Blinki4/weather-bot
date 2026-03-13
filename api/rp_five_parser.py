from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class RpFiveParser:
    KRD_URL = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D0%B5,_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%B0%D0%B9'
    NOVO_URL = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9D%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B5'


    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        self.driver = driver


    # def get_current_weather_krd(self):
    #     self.driver.get(self.KRD_URL)
    #     temp_now = self.driver.find_element(By.XPATH, '//div[@id="ArchTemp"]/child::span[@class="t_0"]').text
    #     return temp_now


    def make_screenshot_krd(self):
        self.driver.get(self.KRD_URL)
        screenshot_path = 'today-weather-krd.png'
        self.driver.get_screenshot_as_file(screenshot_path)
        self.driver.quit()


    def make_screenshot_novo(self):
        self.driver.get(self.NOVO_URL)
        screenshot_path = 'today-weather-novo.png'
        self.driver.get_screenshot_as_file(screenshot_path)
        self.driver.quit()
