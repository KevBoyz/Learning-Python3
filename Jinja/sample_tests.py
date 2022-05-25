import jinja2 as jj
from socket import gethostname, gethostbyname

model = 'Name: {{ name }}, {{ age }} years old'
simple_template = jj.Template(model)

data = [
    ['KevBoyz', 15],
    ['Xanes', 'Undefined']
]

# for person in data:
#     print(template.render(name=person[0], age=person[1]))

# Html with template
loader = jj.FileSystemLoader('templates')
env = jj.Environment(loader=loader)
template = env.get_template('template.html')

render = template.render(title='SwagPage', ip=gethostbyname(gethostname()))
with open('WebPage.html', 'w') as file:
    file.write(render)

