from selenium.webdriver import Firefox
import logging as log
from time import sleep

log.disable()

'''
browser = Firefox()
browser.get('https://apoia.se/livedepython')

h1 = browser.find_element_by_tag_name('h1')

print(h1.text)
'''

# browser.quit()  # Close browser
# x.click # Click in WebElement

_format = '%(levelname)s: %(msg)s'

log.basicConfig(filename='log.log', filemode='w', format=_format, level=log.INFO)

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html#'
browser.get(url)

sleep(6)

a = browser.find_element_by_tag_name('a')
_n = str(browser.find_elements_by_tag_name('p')[-1].text)

log.info(f'a = {a.text}, _n = {_n}')

number = _n[-1]
log.info(f'number = {number}')

while True:
    a.click()
    log.info(f'last = {browser.find_elements_by_tag_name("p")[-1].text},  number = {number}')
    if browser.find_elements_by_tag_name('p')[-1].text[-1] == number:
        break

print('Process Concluded')