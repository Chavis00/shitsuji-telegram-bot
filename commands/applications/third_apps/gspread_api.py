import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from config.config import columns, WORKING_SHEET_ID, SHEET_NAME, CREDS_JSON, SCOPE, CATEGORIES, available_cell
from config.security import check_user_allowed


class Gsheet_Helper:

    def __init__(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_JSON, SCOPE)

        # creds = ServiceAccountCredentials.from_json_keyfile_name(CREEDS, SCOPE)
        # creds = ServiceAccountCredentials._to_json(
        #    CREDS_JSON,
        #    SCOPE
        # )
        self.client = gspread.authorize(creds)
        self.sheet_name = SHEET_NAME
        self.sheet_id = WORKING_SHEET_ID
        self.gsheet = self.client.open_by_key(WORKING_SHEET_ID)
        self.worksheet = self.gsheet.worksheet(self.sheet_name)

        self.desc = ''
        self.category = ''
        self.amount = None
        self.date = None
        self.last_filled_row = None

    def remove_desc(self):
        self.desc = ""

    def update_last_filled_row(self, col):
        self.last_filled_row = len(list(filter(None, self.worksheet.col_values(col))))

    def get_items(self):
        items = self.get_sheet(SHEET_NAME)
        return items

    def get_sheet(self, sheet_name):
        sheet = self.gsheet.worksheet(sheet_name)
        return sheet

    def is_amount(self, arg):
        """ if the arg can be float then it arg is the amount and stop reading args """
        try:
            arg = float(arg)
            self.amount = float(arg)
            return True
        except:
            return False

    def set_category(self, category):
        try:
            self.category = CATEGORIES[category]
        except:
            self.category = None

    def get_data(self, context):
        desc = ''
        is_category = False
        for arg in context.args:
            if is_category:
                self.set_category(arg)
                break
            if self.is_amount(arg):
                """ if arg is amount stop reading args """
                is_category = True
                continue
            desc = desc + arg + ' '
        self.desc = self.desc + desc
        self.date = datetime.today().date()

    def update_sheet(self):

        # example update('A1', value)
        self.worksheet.update(f"{columns['desc']}{self.last_filled_row + 2}",
                              str(self.desc))
        self.worksheet.update(f"{columns['amount']}{self.last_filled_row + 2}",
                              self.amount)
        self.worksheet.update(f"{columns['date']}{self.last_filled_row + 2}",
                              str(self.date))
        self.worksheet.update(f"{columns['category']}{self.last_filled_row + 2}",
                              str(self.category))
        # FORMAT
        self.worksheet.format(
            f"{columns['amount']}",
            {'numberFormat': {
                'type': 'CURRENCY',
                'pattern': '$ #,###.00'
            }})
        self.worksheet.format(f"{columns['date']}",
                              {'numberFormat': {
                                  "type": "DATE_TIME"
                              }})

    @check_user_allowed
    async def spend(self, update, context):
        self.remove_desc()
        self.get_data(context)
        await update.message.reply_text(f"Updating Sheet..")
        try:
            self.update_last_filled_row(1)
            self.update_sheet()
        except:
            await update.message.reply_text("Sorry I can't update sheet :c")
            return

        total = self.worksheet.acell(available_cell).value

        await update.message.reply_text(f"Spent! {total} remaining...")

        return

    @check_user_allowed
    async def total(self, update, context):
        total = self.worksheet.acell(available_cell).value
        await update.message.reply_text(f"{total} remaining...")
        return

    @check_user_allowed
    async def rm_last(self, update, context):
        await update.message.reply_text(f"Removing...")

        self.update_last_filled_row(1)
        self.worksheet.update(f"{columns['desc']}{self.last_filled_row + 1}", '')
        self.worksheet.update(f"{columns['amount']}{self.last_filled_row + 1}",
                              '')
        self.worksheet.update(f"{columns['date']}{self.last_filled_row + 1}", '')
        self.worksheet.update(f"{columns['category']}{self.last_filled_row + 1}",
                              '')
        await update.message.reply_text(f"Removed!")

        return

    def store_tip(self, tip):

        # example update('A1', value)

        self.worksheet.update(f"{columns['tip_ammount']}{self.last_filled_row + 1}",
                              tip)
        self.worksheet.update(f"{columns['tip_date']}{self.last_filled_row + 1}", datetime.now().strftime("%A"))
        # FORMAT
        self.worksheet.format(
            f"{columns['tip_ammount']}",
            {'numberFormat': {
                'type': 'CURRENCY',
                'pattern': '$ #,###.00'
            }})

    @check_user_allowed
    async def add_tip(self, update, context):
        await update.message.reply_text(f"Adding tip..")

        try:
            tip = 0
            for arg in context.args:
                if self.is_amount(arg):
                    tip = float(arg)
                    break
            self.update_last_filled_row(16)
            self.store_tip(tip=tip)
        except Exception as e:
            await update.message.reply_text("Sorry I can't update sheet :c \nbecause: " + str(e))
            return

        total = self.worksheet.acell(available_cell).value

        await update.message.reply_text(f"Tip Added! {total} remaining...")