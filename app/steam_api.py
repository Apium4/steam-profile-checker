import requests


def get_player_summary(api_key, steam_id):
    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"
    params = {
        'key': api_key,
        'steamids': steam_id
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['response']['players'][0] if data['response']['players'] else None
    return None


def get_owned_games(api_key, steam_id):
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        'key': api_key,
        'steamid': steam_id,
        'format': 'json',
        'include_appinfo': True
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json().get('response', {}).get('games', [])
    return []