# SQL
SQL FOR DATA ANALYST
🛠️ Projeto: Análise de Dados com SQLite, SQL e Pandas em Python
🎯 Objetivo do Projeto
O principal objetivo do código é integrar SQLite (um banco de dados leve e eficiente) com Python para manipulação de dados usando SQL e Pandas. Ele realiza consultas SQL diretamente no banco de dados e, depois, compara o mesmo processo usando a sintaxe do Pandas para mostrar como alcançar os mesmos resultados de formas diferentes.

🔧 1. Conexão com o Banco de Dados SQLite
O código estabelece uma conexão com um banco de dados SQLite (cap12_dsa.db) e cria um cursor para percorrer e manipular os dados:

python
Copiar
Editar
con = sqlite3.connect('cap12_dsa.db')
cursor = con.cursor()
O cursor permite executar comandos SQL no banco.

🔍 2. Exploração Inicial das Tabelas
A primeira consulta SQL (sql_query) recupera o nome das tabelas existentes no banco:

python
Copiar
Editar
sql_query = "SELECT name FROM sqlite_master WHERE type = 'table';"
cursor.execute(sql_query)
print(cursor.fetchall())
Isso ajuda a confirmar que a tabela tb_vendas_dsa está disponível para análise.

📊 3. Consultas SQL Direto no Banco de Dados
O código executa várias consultas SQL para análise dos dados:

✅ Consulta 1: Recuperação de todos os dados da tabela
python
Copiar
Editar
query1 = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query1)
Extrai todos os dados da tabela.
Usa uma list comprehension para capturar o nome das colunas dinamicamente:
python
Copiar
Editar
nomes_colunas = [description[0] for description in cursor.description]
📌 Consulta 2: Cálculo da média de unidades vendidas
python
Copiar
Editar
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'
cursor.execute(query2)
AVG é uma função SQL que calcula a média de uma coluna específica.
📌 Consulta 3: Média de unidades vendidas por produto
python
Copiar
Editar
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'
cursor.execute(query3)
GROUP BY agrupa os dados pelo nome do produto.
AVG retorna a média de unidades vendidas para cada produto.
🎯 Consulta 4: Filtro com Condição WHERE
python
Copiar
Editar
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto"""
O WHERE filtra somente produtos com preço unitário maior que 199 antes de calcular a média.
🎯 Consulta 5: Combinação de Filtros com HAVING
python
Copiar
Editar
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""
HAVING aplica uma condição sobre a média calculada (média maior que 10) — isso acontece após o GROUP BY.
🔧 4. Análise Usando Pandas
Agora, o código refaz tudo usando Pandas, sem SQL puro.

📌 Carregamento dos Dados para DataFrame
O código transforma os dados extraídos do banco em um DataFrame do Pandas:

python
Copiar
Editar
df = pd.DataFrame(dados, columns = ['ID_Pedido', 'ID_Cliente', 'Nome_Produto', 'Valor_Unitario', 'Unidades_Vendidas', 'Custo'])
Agora, o DataFrame se comporta como uma tabela manipulável.

📌 Média de Unidades Vendidas (Pandas)
python
Copiar
Editar
media_unidades_vendidas = df['Unidades_Vendidas'].mean()
A versão Pandas da consulta SQL AVG(Unidades_Vendidas).

🎯 Média de Unidades Vendidas por Produto (Pandas)
python
Copiar
Editar
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()
O groupby do Pandas faz o mesmo que o GROUP BY do SQL.
Calcula a média de unidades vendidas para cada produto.
🔥 Filtro de Produtos com Valor Unitário > 199
python
Copiar
Editar
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()
Filtro direto no DataFrame filtra produtos com preço acima de 199 antes de calcular a média.
🔥 Filtro Avançado com Condições Múltiplas (HAVING no Pandas)
Aqui o código replica a complexa combinação do SQL com WHERE + HAVING:

Alternativa A (usando filter()):

python
Copiar
Editar
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)
Alternativa B (encadeando comandos):

python
Copiar
Editar
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()
🧠 5. Comparação Final — SQL vs Pandas
O código termina mostrando a equivalência entre a sintaxe SQL e a do Pandas:

python
Copiar
Editar
# SQL
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""

# Pandas
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()
🔥 Conclusão — O Código Demonstra:
✅ Conexão e manipulação de bancos de dados SQLite com Python.
✅ Consultas SQL avançadas com filtros, agrupamentos e condições.
✅ Conversão dos dados para DataFrame do Pandas.
✅ Realização das mesmas análises com Pandas, comparando com SQL.
