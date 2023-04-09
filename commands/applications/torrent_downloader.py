from torrentp import Downloader
from config.config import TORRENT_PATH
from config.security import check_user_allowed


class Torrent_Downloader:

    def __init__(self):
        pass

    def download_torrent(self, magnet, path):
        torrent_file = Downloader(magnet, path)
        torrent_file.start_download()

    @check_user_allowed
    async def upload_torrent(self, update, context):
        magnet = ""
        for arg in context.args:
                magnet = magnet + arg
        await update.message.reply_text("Downloading...")
        try:
            self.download_torrent(magnet, TORRENT_PATH)
            await update.message.reply_text("Film was added to Plex!")
        except:
            await update.message.reply_text("Something went wrong :c")
