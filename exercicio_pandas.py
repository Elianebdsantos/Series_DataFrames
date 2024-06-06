import pandas as pd

df_vendas = pd.read_pickle('dados_ex1.pkl')


#Exercício 1: Apresente:
#a) O dia com o maior número de vendas e o valor correspondente
print('Data com a maior venda ',df_vendas.idxmax(),df_vendas[df_vendas.idxmax()])
#b) O dia com o menor número de vendas e o valor correspondente
print('Data com a menor venda ',df_vendas.idxmin(),df_vendas[df_vendas.idxmin()])
#c) O valor médio do número de vendas diárias no ano
print('valor medio anual ',df_vendas.mean())
#d) O gráfico da quantidade de vendas diárias

#Exercício 2: A partir da Series do Exercício 1, calcular a média de vendas mensais e
#mostrar o gráfico com a média de vendas mensais. Dica: usar o método `resample()`. O
#que você conclui em relação à variação do número de vendas desse produto ao longo do
#ano?

datas = pd.date_range(start=df_vendas.idxmin(),end=df_vendas.idxmax(),freq='D')

vendas_series = pd.Series(df_vendas,index=datas,name='vendas')

vendas_mensais = vendas_series.resample('ME').mean().round()
vendas_mensais = vendas_mensais.rename('Valores média mensais')
vendas_mensais.plot(grid=True)