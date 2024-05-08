# MongoWeed
Neste trabalho temos a missão de pegar um dataset no Keaggle,
para realizar algumas manipulações usando bancos SQL e NoSQL, 
fazendo uso dos bancos através do docker.
***


 **TASKS:**

* Definição do Dataset (Keaggle)
* Construir modelo lógico (SQL) 
* Construir modelo físico (SQL)
* Aplicar DDL's, DML's e DQL's (SQL) (Docker)
* Dicionário de dados (CSV)
* Fazer passagem de dados (SQL -> NoSQL) (Docker)
* Explicação da tecnologia NoSQL e passagem de dados (PDF)

 ***

 * **PRIMEIRA PARTE: SELEÇÃO DO DATASET**

 Dentre os diversos dataset's disponíveis no Keaggle um nos chamou atenção e decidimos trabalhar com ele.
 O dataset em questão é o "Cannabis Strains" (Justificando o nome dado ao projeto 🌱),
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


 * **SEGUNDA PARTE: CRIAÇÃO DO MODELO LÓGICO**

Para a criação do modelo lógico baseado no SQL tivemos que realizar os processos de normalização
das tabelas, pois os dados do keaggle vinham em modelos colunares e desnormalizados. Após
alguns ajustes e interpretações de dados, chegamos ao seguinte modelo:







![Cannabis](https://github.com/kkaian/MongoWeed/assets/102182718/27a2d827-711f-4311-a461-7fc9789ce999)




(Caso esteja se perguntando, sim, fizemos usando o canva só pela piadinha da folha de fundo)



***

 * **TERCEIRA PARTE: CRIAÇÃO DO MODELO FÍSICO**

 Para o modelo físico não houve piadinhas, foi usado o MySQL Workbanch:

 




![maconha 2](https://github.com/kkaian/MongoWeed/assets/102182718/31cd3a14-cfb3-4c7e-9782-127b8418c2ee)



(uaaaaauuu 🐬🐬🐬)


***


 * **QUARTA PARTE: CRIAÇÃO DAS DDL'S, DML'S, E DQL'S**

**DDL's:**

Esta parte foi realizada através do MySQL Workbanch, após a criação foi adicionado o arquivo 'cannabscript.sql' dentro do código contendo todos a criação do database, que pode ser encontrada na pasta "datannabis" e assim que roda o docker compose é criada pois está especificada no 'volumes'.

*CONSIDERAÇÔES IMPORTANTES:*

*  Você pode encontrar um tutorial para rodar o docker-compose mysql na pasta 'Utilitarios' no arquivo 'dichavador.txt'.
*  O volume está especificando o arquivo usado para criação das DDL's
*  Você pode ter problemas em executar os comandos na porta 3306 caso tenha o 'MySQl Workbanch' instalado na máquina por conta da utilização da porta.

**DML's:**

A inserção de dados na tabela foi feita através de um código python (pytonha-mysql.py) que manipula o arquivo csv (pode ser encontrado em Utilitarios/cannabis.csv) fazendo uso da biblioteca pandas,
depois conecta ao banco criado no docker e insere no mysql as tabelas já normalizadas (isso é incrivel). 

As ações de atualizar e excluir dados podem ser feitas após rodar o docker do mysql com a sintaxe do proprio sql (update, delete).

**DQL's:**

Como o terminal após a rodagem do docker serve como interpretador sql, você pode fazer as consultas por lá. Foi deixado dentro de "datannabis" o arquivo 'Querys_uma_bufa.txt contendo algumas consulas
que podem ser realizadas para testar o banco.

OBS: dentro da pasta "Utilitarios" Você pode encontrar vc pode encontrar o arquivo 'Baga.csv' que é uma versão reduzida do 'cannabis.csv' com apenas 50 registros para a inserção ser mais rápida
(lembre de trocar no pythonha-mysql o caminho do csv).

***

 * **QUINTA PARTE: DICIONÁRIO DE DADOS**

O tratamento de tabelas foi feito através do pandas, mas as tabelas também foram adaptadas para o excel utilizando alguns códigos java. Os códigos com explicação estão na pasta "Utilitarios"
como 'tratannabis1.txt' e 'tratannabis2.txt' e também foi necessária a utilização do site:

https://www.4devs.com.br/remover_trocar_quebra_linha

(Mais detalhes da utilização estão nos arquivos txt)

*Você pode vizualizar tabela em:* https://docs.google.com/spreadsheets/d/1AN3Y1RjH6uOqMchvEOT4V-mCViRbtjSTvznZNiuqHx0/edit?usp=sharing

***
 
 * **SEXTA PARTE: PASSAGEM DE DADOS PARA NOSQL**


A tecnologia escolhida foi o MongoDB 🍃, que no PDF abaixo você pode acompanhar sobre a tecnologia escolhida, como é feita a passagem de dados através do docker como apresentado nos códigos acima, ou caso tenha as plataformas,
utilizando uma ferramenta inovadora, o MongoDb Relational Migrator.

(Os códigos de passagem de dados estão em 'pytonha-mongo.py', as querys + CRUD podem ser encontradas no arquivo 'Querys_chapar' ou podem rodar no terminal seguindo o tutorial do dichavador.txt)

PDF COM EXPLICAÇÃO DA TECNOLOGIA NOSQL E TRANSFERÊNCIA DE DADOS:

https://www.canva.com/design/DAGETpa6esM/TEzhV8nWmG0ZL4UrcT_RUg/edit?utm_content=DAGETpa6esM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton














 
 
