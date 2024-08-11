from selenium.webdriver import Firefox
from urllib.parse import urlparse
from time import sleep
from json import loads

form_data = {
    'nome': 'Kevin',
    'email': 'Kevin@proton-mail.com',
    'senha': '1233456',
    'telefone': '9998875456'
}

browser = Firefox()
url = "https://selenium.dunossauro.live/exercicio_04.html"
browser.get(url)
sleep(5)


def form(nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    sleep(0.3)
    browser.find_element_by_name('email').send_keys(email)
    sleep(0.3)
    browser.find_element_by_name('senha').send_keys(senha)
    sleep(0.3)
    browser.find_element_by_name('telefone').send_keys(telefone)
    sleep(0.3)
    browser.find_element_by_name('btn').click()


form(**form_data)

sleep(2)

# Validating data
print(urlparse(browser.current_url).query.replace('%40', '@').split('&').pop())
result_ = browser.find_element_by_tag_name('textarea').text
result = result_.replace('\'', '\"')

rresult = loads(result)  # Execute string

assert rresult == form_data, 'ERROR: Unsuspected value'