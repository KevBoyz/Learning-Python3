from selenium.webdriver import Firefox
import logging as log

log.basicConfig(filename='log.log', filemode='w', format='%(levelname)s: %(msg)s', level=log.INFO)

browser = Firefox()

url = 'http://localhost:63342/Learning-Python3/Web Scraping/Sites/1ExempleSite.html?_ijt=objnf9acqd3s7m19dqbfhagn2m'
browser.get(url)

ul = browser.find_element_by_tag_name('ul')[0]
log.info(f'ul length: {len(ul)}. Expected: 2')