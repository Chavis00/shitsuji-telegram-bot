from config.config import ALLOWED_USERS_IDS


def check_user_allowed(func):
    async def wrapper(self, update, context):
        if ALLOWED_USERS_IDS == ['ALL']:
            return
        if update.message.from_user.id not in ALLOWED_USERS_IDS:
            await update.message.reply_text("I'm sorry, you are not authorized to use this bot.")
            return
        await func(self, update, context)

    return wrapper
