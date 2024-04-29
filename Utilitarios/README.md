# MongoWeed
Neste trabalho temos a missão de pegar um dataset no Keaggle,
para realizar algumas manipulações usando bancos SQL e NoSQL
***


 **TASKS:**

* Definição do Dataset (Keaggle)
* Construir modelo lógico (SQL) 
* Construir modelo físico (SQL)
* Aplicar DDL's, DML's e DQL's (SQL)
* Fazer passagem de dados (SQL -> NoSQL)
* Explicação da tecnologia NoSQL e passgaem de dados (PDF)

 ***

 **PRIMEIRA PARTE: SELEÇÃO DO DATASET**

 Dentre os diversos dataset's disponíveis no Keaggle um nos chamou atenção e decidimos trabalhar com ele.
 O dataset em questão é o "Cannabis Strains" (Justificando o nome dado ao projeto),
 que consiste em uma gama de 1.27MB de dados sobre tipos de cannabis 🍁
 
-As tabelas em questão são:

* Strain name: Given name of strain

* Type of strain: indica, sativa, hybrid

* Rating: user ratings averaged

* Effects: different effects optained

* Taste: taste of smoke

* Description: backround, etc


Você pode conferir esse dataset em: https://www.kaggle.com/datasets/kingburrito666/cannabis-strains/data

***


 **SEGUNDA PARTE: CRIAÇÃO DO MODELO LÓGICO**

Para a criação do modelo lógico baseado no SQL tivemos que realizar os processos de normalização
das tabelas, pois os dados do keaggle vinham em modelos colunares e desnormalizados. Após
alguns ajustes e interpretações de dados, chegamos ao seguinte modelo:







![Cannabis](https://github.com/kkaian/MongoWeed/assets/102182718/27a2d827-711f-4311-a461-7fc9789ce999)




(Caso esteja se perguntando, sim, fizemos usando o canva só pela piadinha da folha de fundo)



***

 **TERCEIRA PARTE: CRIAÇÃO DO MODELO FÍSICO**

 Para o modelo físico não houve piadinhas, foi usado o MySQL Workbanch:

 




![maconha 2](https://github.com/kkaian/MongoWeed/assets/102182718/31cd3a14-cfb3-4c7e-9782-127b8418c2ee)



(uaaaaauuu 🐬🐬🐬)


***


 **TERCEIRA PARTE: CRIAÇÃO DAS DDL'S, DML'S, E DQL'S**


Esta parte foi realizada atraves do MySQL Workbanch e pode ser encontrada na pasta "DATANNABIS_SQL"

*CONSIDERAÇÔES IMPORTANTES:*

As DML's foram realizadas através da exportação do arquivo .csv para o MySQL, porém os dados que estão na tabela do excel
ainda estão "desnormalizados". Para ajustar, no arquivo txt de "Utilitarios" criei um código em java que separa e filtra os dados que você
pode colar em alguma IDE de java ou compilador online, exibindo no terminal apenas os dados não repetidos para conseguir preencher a tabela n:n.
O código funciona identificando as strings e delimitando pela vírgula.
Caso tenha problemas com quebras de linha, você pode usar o seguinte site para substituir quebras de linha por virgulas:

https://www.4devs.com.br/remover_trocar_quebra_linha  👨‍💻👨‍💻



(em breve criarei outro código para associar os id as strings e prosseguir com o preenchimento)

***

 **QUARTA PARTE: PASSAGEM DE DADOS PARA NOSQL**


A tecnologia escolhida foi o MongoDB 🍃, que no PDF abaixo você pode acompanhar a finalização do projeto, tratando sobre a tecnologia e a passagem de dados.
Mas em resumo a transposição de dados será feita utilizando MongoDb Relational Migrator.

(O PDF ABORDANDO ESTA PARTE DO PROJETO ESTÁ EM PRODUÇÃO E VOCÊ PODE ACOMPANHAR EM:
https://www.canva.com/design/DAGDVjwYESc/DVLPFGNzjC_HSYFLdvwUFg/edit?utm_content=DAGDVjwYESc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton )















 
 
