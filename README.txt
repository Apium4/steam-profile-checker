# Steam Profile Viewer

Приложение для просмотра информации о профиле Steam и списка игр.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/steam-profile-viewer.git
cd steam-profile-viewer

Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

Установите зависимости:
pip install -r requirements.txt

Создайте файл .env на основе примера:
cp .env.example .env

Заполните .env файл своими данными:
STEAM_API_KEY - ваш API ключ от Steam
STEAM_ID - ваш Steam ID

Запустите программу:
flask run

Приложение будет доступно по адресу: http://localhost:5000