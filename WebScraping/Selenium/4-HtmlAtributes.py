from selenium.webdriver import Firefox
from time import sleep


browser = Firefox()
browser.get('https://selenium.dunossauro.live/aula_05_a.html')
sleep(4)

py = browser.find_element_by_id('python')  # Id is what makes a web element unique
# print(py.text)  # Python\n Criada em 1991

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

browser.get('https://selenium.dunossauro.live/aula_05_b.html')
sleep(2)

languages = browser.find_elements_by_class_name('linguagens')  # Return all <div class="linguagens">
for l in languages:   # Find the <h2> for div in languages list and print the text
    print(l.find_element_by_tag_name('h2').text)

# Other global attributes
'''
title
acesskey
autofocus
hidden
'''

browser.get('https://selenium.dunossauro.live/aula_05_c.html')
sleep(2.5)

submit = browser.find_element_by_name('enviar')


def submit_form(film, email, number, submit):
    film_ = browser.find_element_by_name('filme').send_keys(film)
    email_ = browser.find_element_by_name('email').send_keys(email)
    number_ = browser.find_element_by_name('telefone').send_keys(number)
    submit.click()


submit_form('Parasite', 'kevin_pontes@pprint.com', '(088)12345678', submit)