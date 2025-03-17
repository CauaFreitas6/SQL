import sqlite3
import pandas as pd

# CONECTANDO NO BANCO DE DADOS


# Conecta no banco de dados
con = sqlite3.connect('cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

# Query SQL para extrair os nomes das colunas no banco de dados
sql_query = "SELECT name FROM sqlite_master WHERE type = 'table';"

# Executa a query
cursor.execute(sql_query)

# Visualiza o resultado
print(cursor.fetchall())

# A QUERY ABAIXO RETORNA TODAS AS LINHAS E TODAS AS COLUNAS DA TABELA

# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query1)

# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]

# Visualiza o resultado
print(nomes_colunas)

# Retorna os dados da execução da query
dados = cursor.fetchall()

# Visualiza os dados
print(dados)


# Aplicando Linguagem SQL Direto no Banco de dados com python

# A query abaixo retorna a média de unidades vendidas.

# Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query2)

# Visualiza o resultado
print(cursor.fetchall())


# A query abaixo retorna a média de unidades vendidas por produto.

# Cria uma instrução SQL para calcular a média de unidades vendidas por produto.
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'

# Executa a query no banco de dados
cursor.execute(query3)

# Visualiza o resultado
print(cursor.fetchall())


# A query abixo  retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.

# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# Qunado o valor unitário for maior que 199.
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto"""

# Executa a query no banco de dados
cursor.execute(query4)

# Visualiza o resultado
print(cursor.fetchall())


# Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
# Quando o valor unitário for maior que 199, mas somente se a média de unidades vendidas for maior que 10
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""

# Esta é a ordem correta de se usar "SELECT/FROM/WHERE/GROUP BY/HAVING AVG"

#Executa a query no banco de dados
cursor.execute(query5)

# Visualiza o resultado
print(cursor.fetchall())

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()



# APLICANDO LINGUAGEM SQL NA SINTAXE DO PANDAS COM LINGUAGEM PYTHON
# Conecta no banco de dados
con = sqlite3.connect('cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()


# A query abaixo retorna as linhas e todas as colunas da tabela.
# Cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query)

# Retorna os dados da execução da query
dados = cursor.fetchall()

print(dados)

# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido',
                                    'ID_Cliente',
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])

print(df.head())

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()


# A query abaixo retorna a média de unidades vendidas.

# Calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()

print(type(media_unidades_vendidas))
print(media_unidades_vendidas)


# A query abaixo retorno a média de unidades vendidas por produto.

# Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()

# Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produto.head(10))


# A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.

# Retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199.
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()


# A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10.

# Alternativa A
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)

# Alternativa B
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()



# SINTAXE SQL X SINTAXE PANDAS
# As duas instruções abaixo retornam o mesmo resultado!

# Sintaxe SQL
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""

# Sintaxe Pandas
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()