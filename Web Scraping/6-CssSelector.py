from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
b.get('https://selenium.dunossauro.live/aula_06_a.html')
sleep(2)

b.find_element_by_css_selector('[name="nome"]').send_keys('Kevin')
b.find_element_by_css_selector('[name="senha"]').send_keys('123456')

form = b.find_elements_by_css_selector('[class*="form"]')  # Get all elements that have 'form' in class name
form[2].click()

form = b.find_elements_by_css_selector('[type$="t"]')  # Get all elements thar end in 't'
form[1].send_keys('A U T O M A T E')  # TexT, SubmiT

b.find_element_by_css_selector('[name^="s"]').send_keys('the automation')  # Starts with 's'?

b.find_elements_by_css_selector('*')  # Universal selector
b.find_elements_by_css_selector('input[name], label')  # Find multiple elements

# Combinators (selectors)