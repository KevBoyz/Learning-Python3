from selenium.webdriver import Firefox
import logging as log
from time import sleep
from re import search


log.basicConfig(filename='log.log', filemode='w', format='%(levelname)s: %(msg)s', level=log.INFO)

browser = Firefox()

url = 'file:///C:/Users/Kevin/Documents/GitHub/Learning-Python3/Web%20Scraping/Sites/1ExempleSite.html'  # Paste ur path
browser.get(url)

sleep(5)

ul = browser.find_element_by_tag_name('ul')  # First <ul> tag

lis = len(ul.find_elements_by_tag_name('li'))
assert lis == 2, log.error(f'ul(li) length = {lis}. Expected: 2')
log.info(f'ul(li) == {lis}')

li = ul.find_elements_by_tag_name('li')[0]  # <li> [0] Contains ddg link
assert li.text == 'DuckDuckGo', log.error(f'<li> element not found. Value={li.text}, Expected: DuckDuckGo')
log.info(f'li[0].text == {li.text}')

a = li.find_element_by_tag_name('a')  # Finally we can access <a>
log.info(f'<a> [text={a.get_attribute("text")}] href={a.get_attribute("href")}')

# Testing <a>
a.click()  # Work?

browser.get(url)


# Searching element for text

def find_element_by_text(browser, text, tag):
    """
    :param browser: browser instance
    :param text: text to be searched
    :param tag: place that text will searched
    :return: element or 404 if not found
    """
    tags = browser.find_elements_by_tag_name(tag)  # Return list
    for tag in tags:
        if tag.text == text:
            return tag
    return 404


elem = find_element_by_text(browser, 'Text2',  'li')
if elem != 404:
    log.info(f'elem = {elem.text}')
else:
    log.warning(f'elem not found ({elem})')


# Searching  <a> element for href

def find_by_href(browser, link):
    a = browser.find_elements_by_tag_name('a')
    for _link in a:
        if search(link, _link.get_attribute('href')):
            return _link
    return 404


elem2 = find_by_href(browser, 'google')
if elem2 != 404:
    elem2.click()
else:
    log.warning(f'elem not found ({elem2})')

browser.quit()
