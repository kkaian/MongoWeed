import pymongo
from pprint import pprint

# Função para conectar ao MongoDB
def conectar_mongodb():
    # Conectando ao servidor MongoDB (localhost, porta padrão 27017)
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    # Acessando um banco de dados (substitua 'nome_do_banco' pelo nome desejado)
    db = client["mongothc"]
    return db

'''
# Função para fazer uma consulta aos documentos na coleção "Cannabis"
def consultar_documentos_cannabis(db):
    # Consultar todos os documentos na coleção "Cannabis"
    documentos = db["Cannabis"].find()

    # Iterar sobre os documentos e imprimir formatado
    for documento in documentos:
        pprint(documento)

# Conectar ao MongoDB
db = conectar_mongodb()

# Fazer a consulta aos documentos na coleção "Cannabis"
consultar_documentos_cannabis(db)

'''

'''
# Função para exibir documentos com avaliação maior que um valor específico
def mostrar_documentos_avaliacao_maior_que(valor, db):
    filtro = {"avaliacao": {"$gt": valor}}
    for documento in db["Cannabis"].find(filtro):
        pprint(documento)

# Conectar ao MongoDB
db = conectar_mongodb()

# Chamar a função para exibir documentos com avaliação maior que um valor específico (exemplo: 4.0)
mostrar_documentos_avaliacao_maior_que(4.0, db)
'''

'''
# Função para exibir documentos com uma palavra-chave na descrição
def mostrar_documentos_com_palavra_chave(db, palavra_chave):
    filtro = {"descricao": {"$regex": palavra_chave, "$options": "i"}}
    for documento in db["Cannabis"].find(filtro):
        pprint(documento)

# Conectar ao MongoDB
db = conectar_mongodb()

# Chamar a função para exibir documentos com uma palavra-chave na descrição
mostrar_documentos_com_palavra_chave(db, "Earthy")
'''

'''
# Função para inserir um novo documento em uma coleção
def inserir_documento(colecao, documento):
    resultado = colecao.insert_one(documento)
    print("Novo documento inserido com ID:", resultado.inserted_id)

# Exemplo de um novo documento a ser inserido
novo_documento = {
    "tipo": "sativa",
    "nomeVariedade": "Nova Sativa",
    "descricao": "Descrição da nova variedade",
    "avaliacao": 4.5,
    "sabores": ["Citrus", "Pine"],
    "efeitos": ["Energizing", "Euphoric"]
}

# Conectar ao MongoDB
db = conectar_mongodb()

# Chamar a função para inserir um novo documento na coleção "Cannabis"
inserir_documento(db["Cannabis"], novo_documento)
'''

'''
def atualizar_documento(colecao, filtro, novos_valores):
    resultado = colecao.update_one(filtro, {"$set": novos_valores})
    print("Número de documentos atualizados:", resultado.modified_count)

# Conectar ao MongoDB
db = conectar_mongodb()

# Definir o filtro para encontrar o documento a ser atualizado
filtro = {"nomeVariedade": "Nova Sativa"}

# Definir os novos valores a serem atualizados
novo_valor = {"avaliacao": 4.7}

# Chamar a função para atualizar o documento na coleção "Cannabis"
atualizar_documento(db["Cannabis"], filtro, novo_valor)
'''

'''
def excluir_documento(colecao, filtro):
    resultado = colecao.delete_one(filtro)
    print("Número de documentos excluídos:", resultado.deleted_count)

# Conectar ao MongoDB
db = conectar_mongodb()

# Definir o filtro para encontrar o documento a ser excluído
filtro = {"nomeVariedade": "Nova Sativa"}

# Chamar a função para excluir o documento na coleção "Cannabis"
excluir_documento(db["Cannabis"], filtro)

'''