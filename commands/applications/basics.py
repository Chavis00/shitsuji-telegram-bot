import logging

from telegram.ext import Application, ContextTypes, MessageHandler, filters
from telegram import ForceReply, Update

"""
Basic Bot Functions
update: handles the bot
context:
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        "/spend <desc> <amount> <category> updates google sheet \n/total returns total \n/rm removes last spend\n/recipe <food> returns random recipe\n/tip <tip> add a new tip\n/torrent <magnet> donwload and add new film to Plex")


async def me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = "Your id is " + str(update._effective_user.id)
    logging.info(msg=msg)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)
