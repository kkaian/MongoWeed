import mysql.connector
import pandas as pd

arquivo_csv = 'Utilitarios/cannabis.csv'

# Ler o arquivo CSV e carregar os dados em um DataFrame do Pandas
df = pd.read_csv(arquivo_csv)

# Exibir as primeiras linhas do DataFrame para verificar a leitura correta
print(df.head())

# Configurações de conexão com o MySQL
config = {
    'user': 'root',
    'password': 'bobmarley420',
    'host': 'localhost',
    'port': 3306,
    'database': 'mysqlombra'
}

# Estabelecer conexão com o MySQL
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Inserir os dados do DataFrame no MySQL
for index, row in df.iterrows():
    sql = "INSERT INTO Cannabis (tipo) VALUES (%s)"
    values = (row['tipo'],)
    cursor.execute(sql, values)


# Commit das alterações
conn.commit()

# Fechar conexão
cursor.close()
conn.close()
