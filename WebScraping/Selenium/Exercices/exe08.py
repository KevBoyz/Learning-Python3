from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

b = Firefox()
b.get('https://selenium.dunossauro.live/exercicio_08.html')
sleep(10)

box = b.find_element_by_id('caixa')
text_area = b.find_element_by_id('area')

ac = ActionChains(b)


def clicks(key1=Keys.SHIFT, key2=Keys.CONTROL):
    # Simple click
    ac.move_to_element(box)
    ac.click(box)
    ac.move_to_element(text_area)

    # More clicks
    ac.move_to_element(box)
    ac.double_click(box)
    ac.context_click(box)
    ac.click(box)
    ac.move_to_element(text_area)

    # key1
    ac.key_down(key1)
    ac.move_to_element(box)
    ac.click(box)
    ac.double_click()
    ac.move_to_element(text_area)
    ac.key_up(key1)

    # key2
    ac.key_down(key2)
    ac.move_to_element(box)
    ac.click(box)
    ac.double_click()
    ac.move_to_element(text_area)
    ac.key_up(key2)

    # key1 + key2
    ac.key_down(key1)
    ac.key_down(key2)
    ac.move_to_element(box)
    ac.click(box)
    ac.double_click()
    ac.move_to_element(text_area)
    ac.key_up(key1)
    ac.key_down(key2)

    ac.perform()



clicks()