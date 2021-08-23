from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from functools import partial


f = Chrome()
# f.implicitly_wait(15)

wdw = WebDriverWait(f, 30, 2)


def wait(element, by, webdriver):
    print(f'Trying find "{element}" by {by}')
    if webdriver.find_elements(by, element):
        return True
    return False


f.get('https://selenium.dunossauro.live/aula_09_a.html')
wdw.until(partial(wait, 'button', By.CSS_SELECTOR), 'this program sucks')

f.find_element_by_css_selector('button').click()

wdw.until(partial(wait, '#finished', By.CSS_SELECTOR))

fns = f.find_element_by_css_selector('#finished')
assert fns.text == 'Carregamento concluído'