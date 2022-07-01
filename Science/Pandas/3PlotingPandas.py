import pandas as pd
from matplotlib import pyplot as plt

vendas = pd.read_excel('assets/Vendas.xlsx')
norte_shopping = vendas.loc[vendas['ID Loja'] == 'Norte Shopping', ['Data', 'Quantidade', 'Valor Final']]
norte_shopping.dropna()
norte_shopping = norte_shopping.groupby('Data').sum()
print(norte_shopping)


plt.style.use("seaborn-dark")

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey

fig, ax = plt.subplots()
ax.grid(color='#2A3459')  # bluish dark grey, but slightly lighter than background
colors = [
    '#08F7FE',  # teal/cyan
    '#FE53BB',  # pink
    '#F5D300',  # yellow
    '#00ff41'   # matrix green
]
plt.xticks(rotation=30)

plt.plot(norte_shopping['Quantidade'] * 20, '--.', label='Produtos vendidos', color=colors[3])
plt.plot(norte_shopping['Valor Final'], '--.', label='Valor arrecadado', color=colors[0])
plt.plot((norte_shopping['Valor Final'] / norte_shopping['Quantidade']) * 20, linestyle='dotted', color=colors[1], label='Vendas/faturamento', marker='.')
plt.title('Norte Shopping - Vendas 01/01 - 07/02')
plt.legend(loc="upper left")
plt.show()
