# Shitsuji Telegram Bot
This Telegram bot exists with the sole purpose of helping you with your daily life. 'Shitsuji' means 'butler' in Japanese, and that's the goal of this bot. Currently, it has three different applications that have the sole purpose of helping you.

## Application Overview
Currently, the bot has 3 applications that can be used:

- RECIPE: An application connected to an Edamam API where a food is passed as a parameter and it returns the necessary ingredients and recipe URL for recipes with similar names.
- TORRENT: A basic application where a magnet link is passed to the bot and it downloads the torrent to the configured directory. Initially, it was used to download movies to a Plex server.
- GSHEET: An application to load your expenses into a customizable Google Sheets spreadsheet, allowing you to have full control over the amount of money available, even if it's spread across various accounts or cash. Classifiable expenses can be made with a simple command, and when the spreadsheet is updated, the graphs in it are also modified, giving you better control over your expenses.

It is not necessary to use or have all 3 applications configured. To choose which applications the bot will use, you need to change the following in config.py:
```python
INSTALLED_APPS = ['GSHEET', 'RECIPE', 'TORRENT']
```
## Security
By default, the bot will not allow you to use the commands as they are protected. To be able to use the reserved commands, the user IDs authorized to do so must first be configured in config.py.
```py
ALLOWED_USERS_IDS = [
    1234567890,
    1234567890,
    1234567890
]
# NOT RECOMENDED but If you want to allow any user to use the commands, 
# simply configure as follows:
ALLOWED_USERS_IDS = ['ALL']
```
If you want to know your user ID, you can use the bot command /me and check the logs of the container, which will print the sender ID
## Application Configuration
### Telegram Bot Configuration
Send a Telegram message to @BotFather and type /newbot, then configure your token in enviroment variables
```dosini
BOT_TOKEN=yourownbottoken
```
### Recipe API Configuration
To get your credentials to use /recipe command you must to signup  [here](https://developer.edamam.com/edamam-recipe-api), create a new application using "Recipe Search API" and then configure in your enviroment variables
```dosini
RECIPE_URL=https://api.edamam.com/api/recipes/v2 general like this
RECIPE_APP_ID=yourid
RECIPE_APP_KEY=yourkey
```
You will have 10,000 API calls per month, which should be enough for personal use.

### Torrent Downloader Configuration
The easier configuration, just change the directory in config.py 
```python
TORRENT_PATH = "/your/path"
```

### Google Sheets Configuration
This is my [template](https://docs.google.com/spreadsheets/d/15h8PVqjONZ7YIqVe49lz_QLOQjV6hS1-fuSnOlaadzI/edit#gid=0), just copy and enjoy!

To get your credentials to use google sheet commands you need to 
- Visit to your [Google Cloud Console](https://console.cloud.google.com/welcome)
- Create your own project
- On the search bar type "Google Sheets API" and select the marketplace option
- Select "Enable"
- Search for "Credentials" and create a new one selecting the option "Service Account"
- Complete the first requirements fields (Only account name needed)
- Last requirement is Key, select "Create Key" 
- Select "Json" , and then complete
- The JSON file should have been downloaded, seach the value of client_email and copy
- Share your google sheet with the email you copy, give editor role

Once you get your JSON file now you can rename it creds.json or change it in config.py:
```python
CREDS_JSON = '/path/to/creds.json'
```
Check your WORKING_SHEET_ID on the URL of your sheet 

```dosini
https://docs.google.com/spreadsheets/d/{WORKING_SHEET_ID}/edit#gid=123123
```
And then set your enviroment variables, 
```dosini
WORKING_SHEET_ID=yourworkingsheetid
SHEET_NAME=currentsheetname
```


You can check the usage limits [here](https://developers.google.com/sheets/api/limits), but again for personal use should be enough

| Quotas         | Description                     | Limit | 
|----------------|---------------------------------|-------|
| Read requests  | Per minute per project          | 300   |
|                | Per minute per user per project | 60    | 
| Write requests | Per minute per project          | 300   |
|                | Per minute per user per projec  | 60    |

# How to use
## Run with Docker
### Build Docker Image
```
docker build -t 'shitsuji' .
```
Execute the following command to run the script, making sure to correctly add the environment variables if necessary:
```
 docker run --name shitsuji \
  -e BOT_TOKEN=yourbottoken \
  -e WORKING_SHEET_ID=yourworkingsheet \
  -e SHEET_NAME=yoursheetname \
  -e RECIPE_URL=recipeapiurl \
  -e RECIPE_APP_ID=recipeid \
  -e RECIPE_APP_KEY=recipekey \
  -e TZ=yourtimezone \
  shitsuji
```

## Run with docker-compose
Configure your .env file and then run
```
docker-compose up --build
```