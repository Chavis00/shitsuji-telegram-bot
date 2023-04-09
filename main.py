from config.config import TOKEN
from telegram.ext import Application
from commands.commands_handler import add_commands
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def start_bot() -> None:
    application = Application.builder().token(TOKEN).build()
    add_commands(application)
    application.run_polling()


if __name__ == '__main__':
    start_bot()
