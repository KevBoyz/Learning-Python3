import pandas as pd
from matplotlib import pyplot as plt

vendas = pd.read_excel('assets/Vendas.xlsx')
norte_shopping = vendas.loc[vendas['ID Loja'] == 'Norte Shopping', ['Data', 'Quantidade', 'Valor Final']]
norte_shopping.dropna()
norte_shopping = norte_shopping.groupby('Data').sum()
print(norte_shopping)

plt.plot(norte_shopping['Quantidade'] * 20, 'b--o', label='Produtos vendidos')
plt.plot(norte_shopping['Valor Final'], 'r-o', label='Valor arrecadado')
plt.plot((norte_shopping['Valor Final'] / norte_shopping['Quantidade']) * 20, linestyle='dotted', color='green', label='Vendas/faturamento')
plt.title('Norte Shopping - Vendas 01/01 - 07/02')
plt.legend(loc="upper left")
plt.show()
