FROM mariadb
ENV MYSQL_DATABASE=TP_INFRA \ MYSQL_ROOT_PASSWORD=root_password
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/
EXPOSE 3306