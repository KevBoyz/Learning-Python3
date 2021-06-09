from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


b = Firefox()
ac = ActionChains(b)  # Low-level api
# b.get('https://selenium.dunossauro.live/keyboard')
# sleep(5)


# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys  --Unicode

'''
# Hi-level
html = b.find_element_by_tag_name('html')
html.send_keys('kevin')
'''

b.get('https://selenium.dunossauro.live/aula_08_a')
sleep(3)

# Hi-level
text_box = b.find_element_by_name('texto')  # Needs find element in hi-level

# Low-level api
ac.move_to_element(text_box)
ac.click(text_box)  # Click to active Focus event (Don't work without this)


def type_with(text, key):
    ac.key_down(key)
    for letter in text:
        ac.key_down(letter)
        ac.key_up(letter)
    ac.key_up(key)
    ac.perform()


type_with('Selenium', Keys.SHIFT)  # Equal u'\ue008'
b.quit()

# Mouse events

b = Firefox()
b.get('https://selenium.dunossauro.live/caixinha')
sleep(6)

box = b.find_element_by_id('caixa')
span = b.find_element_by_tag_name('span')

ac = ActionChains(b)


def boxx(key):
    ac.key_down(key)
    ac.move_to_element(box)  # Mouse enter
    ac.click(box)
    ac.pause(0.5)
    ac.double_click(box)
    ac.pause(0.5)
    ac.context_click(box)
    ac.pause(0.5)
    ac.move_to_element(span)  # Mouse leave
    ac.perform()
    ac.key_up(key)


boxx(Keys.SHIFT)
boxx(Keys.CONTROL)


