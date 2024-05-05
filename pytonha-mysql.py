import mysql.connector
import pandas as pd
import numpy as np

arquivo_csv = 'Utilitarios/baga.csv'

# Ler o arquivo CSV e carregar os dados em um DataFrame do Pandas
df = pd.read_csv(arquivo_csv)

# Substituir valores NaN por None em todo o DataFrame
df = df.where(pd.notnull(df), None)

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

# Adicionar restrições únicas às colunas de efeitoCannabis e saborCannabis
cursor.execute("ALTER TABLE Efeitos ADD UNIQUE (efeitoCannabis)")
cursor.execute("ALTER TABLE Sabores ADD UNIQUE (saborCannabis)")

# Salvar as alterações
conn.commit()

# Loop através das linhas do DataFrame
for index, row in df.iterrows():
    tipo = row['Type']
    variedade = row['Strain']
    descricao = row['Description']
    avaliacao = row['Rating']
    
    
    # Inserir os dados na tabela Cannabis
    cursor.execute("INSERT INTO Cannabis (tipo) VALUES (%s)", (tipo,))
    conn.commit()

    # Obter o último ID inserido na tabela Cannabis
    cursor.execute("SELECT LAST_INSERT_ID()")
    cannabis_id = cursor.fetchone()[0]

    # Inserir os dados na tabela Variedade, usando o último ID inserido na tabela Cannabis
    cursor.execute("INSERT INTO Variedade (nomeVariedade, descricao, avaliacao, Cannabis_idCannabis) VALUES (%s, %s, %s, %s)", (variedade, descricao, avaliacao, cannabis_id))
    conn.commit()

    variedade_id = cursor.execute("SELECT LAST_INSERT_ID()")
    variedade_id = cursor.fetchone()[0]
    

    # Relacionar os efeitos com a variedade
     # **Verificar se o valor em 'Effects' é uma string**
    # Relacionar os efeitos com a variedade
    if isinstance(row['Effects'], str):
        for efeito in row['Effects'].split(','):
            # Verificar se o efeito já existe
            cursor.execute("SELECT idEfeito FROM Efeitos WHERE efeitoCannabis = %s", (efeito,))
            efeito_id = cursor.fetchone()
            cursor.fetchall()

            # Se o efeito não existe, inserir na tabela Efeitos e obter o ID
            if not efeito_id:
                cursor.execute("INSERT INTO Efeitos (efeitoCannabis) VALUES (%s)", (efeito,))
                conn.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                efeito_id = cursor.fetchone()[0]
            else:
                efeito_id = efeito_id[0]

            # Relacionar o efeito com a variedade na tabela de relação Efeito_Variedade
            cursor.execute("INSERT INTO Efeito_Variedade (Efeitos_idEfeito, Variedade_idVariedade) VALUES (%s, %s)", (efeito_id, variedade_id))
            conn.commit()
    else:
        # Se 'Effects' não for uma string, tratar como 'None'
        cursor.execute("SELECT idEfeito FROM Efeitos WHERE efeitoCannabis = 'None'")
        efeito_none = cursor.fetchone()
        if not efeito_none:
            # Se 'None' não existir na tabela Efeitos, inserir
            cursor.execute("INSERT INTO Efeitos (efeitoCannabis) VALUES ('None')")
            conn.commit()
            # Obter o ID do efeito 'None'
            cursor.execute("SELECT LAST_INSERT_ID()")
            efeito_id = cursor.fetchone()[0]
        else:
            efeito_id = efeito_none[0]

        # Relacionar o efeito 'None' com a variedade na tabela de relação Efeito_Variedade
        cursor.execute("INSERT INTO Efeito_Variedade (Efeitos_idEfeito, Variedade_idVariedade) VALUES (%s, %s)", (efeito_id, variedade_id))
        conn.commit()
    # Relacionar os sabores com a variedade
    if isinstance(row['Flavor'], str):
        for sabor in row['Flavor'].split(','):
            # Verificar se o sabor já existe
            cursor.execute("SELECT idSabor FROM Sabores WHERE saborCannabis = %s", (sabor,))
            sabor_id = cursor.fetchone()
            cursor.fetchall()
            # Se o sabor não existe, inserir na tabela Sabores e obter o ID
            if not sabor_id:
                cursor.execute("INSERT INTO Sabores (saborCannabis) VALUES (%s)", (sabor,))
                conn.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                sabor_id = cursor.fetchone()[0]
            else:
                sabor_id = sabor_id[0]

            # Relacionar o sabor com a variedade na tabela de relação Sabor_Variedade
            cursor.execute("INSERT INTO Sabor_Variedade (Sabores_idSabor, Variedade_idVariedade) VALUES (%s, %s)", (sabor_id, variedade_id))
            conn.commit()
    else:
        # Se 'Flavor' não for uma string, tratar como 'None'
        cursor.execute("SELECT idSabor FROM Sabores WHERE saborCannabis = 'None'")
        sabor_none = cursor.fetchone()
        if not sabor_none:
            # Se 'None' não existir na tabela Sabores, inserir
            cursor.execute("INSERT INTO Sabores (saborCannabis) VALUES ('None')")
            conn.commit()
            # Obter o ID do sabor 'None'
            cursor.execute("SELECT LAST_INSERT_ID()")
            sabor_id = cursor.fetchone()[0]
        else:
            sabor_id = sabor_none[0]

        # Relacionar o sabor 'None' com a variedade na tabela de relação Sabor_Variedade
        cursor.execute("INSERT INTO Sabor_Variedade (Sabores_idSabor, Variedade_idVariedade) VALUES (%s, %s)", (sabor_id, variedade_id))
        conn.commit()
# Fechar conexão
cursor.close()
conn.close()