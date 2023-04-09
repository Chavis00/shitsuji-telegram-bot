import requests
import random

from config.security import check_user_allowed
from errors.errors import unable_connect_api
from config.config import RECIPE_URL, RECIPE_APP_ID, RECIPE_APP_KEY


class RecipeAPI:
    def __init__(self):
        self.url = RECIPE_URL
        self.app_id = RECIPE_APP_ID
        self.api_key = RECIPE_APP_KEY
        self.recipe = None
        self.ingredients = None

    def get_response(self, food):
        try:
            payload = {
                'type': 'public',
                'q': food,
                'app_id': self.app_id,
                'app_key': self.api_key
            }
            response = requests.get(url=self.url, params=payload).json()
            return response
        except:
            msg = unable_connect_api(self)
            return msg

    def random_recipe(self, recipes):
        """  """
        rand_int = random.randint(0, len(recipes['hits']))
        recipe = str(recipes['hits'][rand_int - 1]['recipe']['url'])
        ingredients = recipes['hits'][rand_int - 1]['recipe']['ingredientLines']

        return recipe, ingredients

    def get_recipe(self, food):
        """ Get """
        print(food)
        recipes = self.get_response(food)

        if len(recipes['hits']) < 1:
            return "I don't have that recipe :c"

        self.recipe, self.ingredients = self.random_recipe(recipes)

        self.order_ingredients()

    @check_user_allowed
    async def send_recipe(self, update, context):
        """ Send a random recipe from edaman recipes """
        try:
            food = ''
            for arg in context.args:
                food = food + arg + ' '
        except:
            await update.message.reply_text("Please send the recipe you are looking for...")
            return
        try:
            self.get_recipe(food)
        except:
            self.get_recipe(food)

            await update.message.reply_text("Something went wrong with API credentials :c")
            return

        await update.message.reply_text(self.recipe)
        await update.message.reply_text(self.ingredients)

    def order_ingredients(self):
        order_ingredients = ''
        for ingredient in self.ingredients:
            new_ingredient = "\n+ " + ingredient
            order_ingredients = order_ingredients + new_ingredient
        self.ingredients = order_ingredients
