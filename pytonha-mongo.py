import pymongo
import mysql.connector
from decimal import Decimal

# Função para conectar ao MongoDB
def conectar_mongodb():
    # Conectando ao servidor MongoDB (localhost, porta padrão 27017)
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Acessando um banco de dados (substitua 'nome_do_banco' pelo nome desejado)
    db = client["mongothc"]
    return db

# Função para importar dados do MySQL e desnormalizá-los
def importar_desnormalizar_mysql(db):
    # Configurações de conexão com o MySQL
    config_mysql = {
        'user': 'root',
        'password': 'bobmarley420',
        'host': 'localhost',
        'port': 3306,
        'database': 'mysqlombra'
    }

    # Estabelecer conexão com o MySQL
    conn_mysql = mysql.connector.connect(**config_mysql)
    cursor_mysql = conn_mysql.cursor()

    # Query para selecionar os dados normalizados do MySQL
    query = """
        SELECT Cannabis.tipo, Variedade.nomeVariedade, Variedade.descricao, Variedade.avaliacao, GROUP_CONCAT(DISTINCT Sabores.saborCannabis) AS sabores, GROUP_CONCAT(DISTINCT Efeitos.efeitoCannabis) AS efeitos
        FROM Variedade
        JOIN Cannabis ON Variedade.Cannabis_idCannabis = Cannabis.idCannabis
        LEFT JOIN Sabor_Variedade ON Variedade.idVariedade = Sabor_Variedade.Variedade_idVariedade
        LEFT JOIN Sabores ON Sabor_Variedade.Sabores_idSabor = Sabores.idSabor
        LEFT JOIN Efeito_Variedade ON Variedade.idVariedade = Efeito_Variedade.Variedade_idVariedade
        LEFT JOIN Efeitos ON Efeito_Variedade.Efeitos_idEfeito = Efeitos.idEfeito
        GROUP BY Variedade.idVariedade;
    """

    # Executar a query no MySQL
    cursor_mysql.execute(query)

    # Coleção para armazenar os dados de variedades de cannabis
    collection_variedades = db["Cannabis"]

    # Loop através das linhas retornadas pela query do MySQL
    for row in cursor_mysql.fetchall():
        # Converter Decimal para float
        avaliacao = float(row[3]) if row[3] is not None else None

        # Criando documento para inserção no MongoDB
        documento = {
            "tipo": row[0],
            "nomeVariedade": row[1],
            "descricao": row[2],
            "avaliacao": avaliacao,
            "sabores": row[4].split(',') if row[4] else [],
            "efeitos": row[5].split(',') if row[5] else []
        }
        # Inserindo o documento na coleção de variedades
        collection_variedades.insert_one(documento)

    # Fechar conexão com o MySQL
    cursor_mysql.close()
    conn_mysql.close()

# Conectar ao MongoDB
db = conectar_mongodb()

# Importar dados do MySQL e desnormalizá-los
importar_desnormalizar_mysql(db)

print("Dados importados e desnormalizados com sucesso do MySQL para o MongoDB.")
