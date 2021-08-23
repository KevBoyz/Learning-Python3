from selenium.webdriver import Firefox
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
import logging as log
from time import sleep

log.basicConfig(filename='log.log', filemode='w', format='%(levelname)s: %(msg)s', level=log.INFO)


class Listener(AbstractEventListener):

    def after_navigate_to(self, url, driver):
        log.info(url)

    def before_click(self, element, driver):
        log.info(f'[{element.get_attribute("id")}] Before: \'{driver.find_element_by_id(f"l" + element.get_attribute("id")).text}\'')

    def after_click(self, element, driver):
        log.info(
            f'[{element.get_attribute("id")}] After: \'{driver.find_element_by_id(f"l" + element.get_attribute("id")).text}\'')



b = EventFiringWebDriver(Firefox(), Listener())  # Fire browser

b.get('https://selenium.dunossauro.live/exercicio_07.html')
sleep(10)


input_1 = b.find_element_by_css_selector('input#nome')
input_1.click()
input_1.send_keys('Kevin')

input_2 = b.find_element_by_css_selector('input#email')
input_2.click()
input_2.send_keys('Kevinho_PPontes@ddg.gg')

input_3 = b.find_element_by_css_selector('input#senha')
input_3.click()
input_3.send_keys('115x712')

try:
    button = b.find_element_by_id('btn')
except:
    pass