import os

""" Application """
ALLOWED_USERS_IDS = [1499495357]
INSTALLED_APPS = ['GSHEET', 'RECIPE', 'TORRENT']

""" Telegram """
TOKEN = os.getenv('BOT_TOKEN')

""" Sheet Settings """
columns = {
    'desc': 'A',
    'amount': 'C',
    'date': 'D',
    'category': 'B',
    'tip_ammount': 'P',
    'tip_date': 'Q',
}
available_cell = 'H10'

CATEGORIES = {
    'ren': 'Rent',
    'foo': 'Food',
    'ser': 'Services',
    'hou': 'House',
    'res': 'Restaurant',
    'sub': 'Substance',
    'tre': 'Treats',
    'hyg': 'Hygiene',
    'med': 'Medicine',
    'pet': 'Pet',
    'clo': 'Cloth'

}

""" Google Sheet """
WORKING_SHEET_ID = os.environ.get('WORKING_SHEET_ID')
SHEET_NAME = os.environ.get('SHEET_NAME')
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

""" Recipe API  """
RECIPE_URL = os.environ.get('RECIPE_URL')
RECIPE_APP_ID = os.environ.get('RECIPE_APP_ID')
RECIPE_APP_KEY = os.environ.get('RECIPE_APP_KEY')
CREDS_JSON = 'creds.json'

""" Torrent Downloader """
TORRENT_PATH = "/code/Films"