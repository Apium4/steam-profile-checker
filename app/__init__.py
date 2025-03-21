from flask import Flask
from flask_caching import Cache  # Импортируем класс Cache
from dotenv import load_dotenv

load_dotenv()

# Создаём экземпляр кэша
cache = Cache()


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object('app.config.Config')

    # Инициализируем кэш с приложением
    cache.init_app(app)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app