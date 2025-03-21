import os

class Config:
    STEAM_API_KEY = os.getenv('STEAM_API_KEY')
    STEAM_ID = os.getenv('STEAM_ID')
    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300