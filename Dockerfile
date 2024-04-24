FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./datannabis/cannabscript.sql /docker-entrypoint-initdb.d/cannabscript.sql 