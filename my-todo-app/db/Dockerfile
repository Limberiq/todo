# db/Dockerfile

# Используем официальный образ PostgreSQL 13 в качестве базового
FROM postgres:13

# Устанавливаем переменные окружения для пользователя, пароля и имени базы данных
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=todo

# Копируем SQL-скрипт инициализации в специальную директорию, откуда он будет выполнен при запуске контейнера
COPY init.sql /docker-entrypoint-initdb.d/