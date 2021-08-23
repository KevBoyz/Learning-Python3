from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep

browser = Firefox()
url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser.get(url)

sleep(10)


def main():
    return browser.find_element_by_tag_name('main')


# First step
main().find_element_by_tag_name('a').click()
sleep(2)

# Second step
text = main().find_elements_by_tag_name('p')[1].text

n1 = int(text[0])
n2 = int(text[-3])
_as = main().find_elements_by_tag_name('a')

if str(n1 * n2) != _as[0].text:
    _as[0].click()
else:
    _as[1].click()
sleep(60)

# Third step
title = browser.title
_as = main().find_elements_by_tag_name('a')

if _as[0].text == title:
    _as[0].click()
else:
    _as[1].click()
sleep(5)

# Four step
path = urlparse('https://selenium.dunossauro.live/page_3.html').path
_as = main().find_elements_by_tag_name('a')

if '/' + _as[0].text == path:
    _as[0].click()
else:
    assert '/' + _as[0].text != path, 'Error: Value not found'
sleep(2)

# Five step
browser.refresh()