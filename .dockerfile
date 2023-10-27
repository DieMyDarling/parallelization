# Используем базовый образ Python
FROM python:3.8

# Устанавливаем переменную окружения для предотвращения вывода лишних предупреждений
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости с помощью pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы вашего проекта в рабочую директорию
COPY . /app/

# Запускаем приложение
CMD ["pytest"]
