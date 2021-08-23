from selenium.webdriver import Firefox
from time import sleep

b = Firefox()
b.get('https://selenium.dunossauro.live/exercicio_06.html')

sleep(7)


def do(n):
    get_forms = b.find_elements_by_css_selector('div#grid > form[class*="form-"')
    divs = get_forms[n].find_elements_by_css_selector('div[class*="form-"]')
    divs[0].find_element_by_css_selector('input[name="nome"').send_keys('Kevin')
    sleep(0.1)
    divs[1].find_element_by_css_selector('input[name="senha"').send_keys('12345')
    sleep(0.1)
    divs[2].find_element_by_css_selector('input[value="Enviar!"]').click()


value = b.find_element_by_css_selector('header > p > span').text
while value != '... Mentira, você conseguiu terminar':
    value = b.find_element_by_css_selector('header > p > span').text
    if value == '... Mentira, você conseguiu terminar':
        break
    elif value == 'l0c0':
        n = 0
    elif value == 'l1c0':
        n = 1
    elif value == 'l0c1':
        n = 2
    else:
        n = 3
    do(n)
    sleep(0.4)

