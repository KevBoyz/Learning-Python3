from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep


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


browser = Firefox()
browser.get('https://selenium.dunossauro.live/aula_04_b.html')  # Change 'a' -> 'b' to see the path

sleep(1)

parse = urlparse(browser.current_url)

print(parse.scheme)
print(parse.netloc)
print(parse.path)  # Empty path

browser.refresh()  # Update the page

print(browser.title)  # Page title

'''
c = 0
while True:
    for text in ['um', 'dois', 'tres', 'quatro']:
        find_element_by_text(browser, text, 'div').click()
    while c < 30:                                                # Auto clicker
        for c in range(0, 4):
            browser.back()
        for c in range(0, 4):
            browser.forward()
'''
