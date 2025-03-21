from flask import Blueprint, render_template
from app import cache
from app.steam_api import get_player_summary, get_owned_games
import os

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
@cache.cached(timeout=300)
def index():
    api_key = os.getenv('STEAM_API_KEY')
    steam_id = os.getenv('STEAM_ID')

    profile_info = get_player_summary(api_key, steam_id)
    games = get_owned_games(api_key, steam_id)

    return render_template('profile.html',
                           profile_info=profile_info,
                           games=games)


@main_bp.route('/update')
def update():
    cache.delete('view//')  # Очистка кэша для главной страницы
    return index()