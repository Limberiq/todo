# Используем официальный образ Python в качестве базового
FROM python:3.9

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы в рабочую директорию
COPY . .

# Указываем команду для запуска приложения
CMD ["python", "app.py"]