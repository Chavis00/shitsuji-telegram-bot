from telegram.ext import Application
from telegram.ext import CommandHandler

from commands.applications import basics
from commands.applications.torrent_downloader import Torrent_Downloader
from config.config import INSTALLED_APPS


def add_commands(telegram_bot: Application) -> None:
    telegram_bot.add_handler(CommandHandler("start", basics.start))
    telegram_bot.add_handler(CommandHandler("help", basics.help))
    telegram_bot.add_handler(CommandHandler("me", basics.me))

    if 'TORRENT' in INSTALLED_APPS:
        torrent = Torrent_Downloader()
        telegram_bot.add_handler(CommandHandler("torrent", torrent.upload_torrent))

    if 'GSHEET' in INSTALLED_APPS:
        from commands.applications.third_apps.gspread_api import Gsheet_Helper
        gspread_api = Gsheet_Helper()
        telegram_bot.add_handler(CommandHandler("spend", gspread_api.spend))
        telegram_bot.add_handler(CommandHandler("tip", gspread_api.add_tip))
        telegram_bot.add_handler(CommandHandler("total", gspread_api.total))
        telegram_bot.add_handler(CommandHandler("rm", gspread_api.rm_last))

    if 'RECIPE' in INSTALLED_APPS:
        from commands.applications.third_apps.recipe_api import RecipeAPI
        recipe_api = RecipeAPI()
        telegram_bot.add_handler(CommandHandler("recipe", recipe_api.send_recipe))
