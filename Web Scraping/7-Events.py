from selenium.webdriver import Firefox
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
import pyautogui
import logging as log
from time import sleep

log.basicConfig(filename='log.log', filemode='w', format='%(levelname)s: %(msg)s', level=log.INFO)


class Listener(AbstractEventListener):

    def after_navigate_to(self, url, driver):
        log.info(url)

    def before_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            log.info(f'[input click] Before: span<{webdriver.find_element_by_tag_name("span").text}>')

    def after_click(self, elemento, webdriver):
        if elemento.tag_name == 'input':
            log.info(f'[input click] After: span<{webdriver.find_element_by_tag_name("span").text}>')


fire_b = EventFiringWebDriver(Firefox(), Listener())  # Fire browser

fire_b.get('https://selenium.dunossauro.live/aula_07_d.html')
sleep(10)

input_ = fire_b.find_element_by_tag_name('input')
span = fire_b.find_element_by_tag_name('span').text

input_.click()
input_.send_keys('Kevin')
pyautogui.press('enter')
pyautogui.click(x=276, y=229)