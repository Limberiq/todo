-- db/init.sql

-- Создаем таблицу todo с двумя колонками: id и task
CREATE TABLE todo (
    id SERIAL PRIMARY KEY,
    task VARCHAR(80) NOT NULL
);