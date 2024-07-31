import logging

import certifi
from dotenv import dotenv_values
from pymongo import MongoClient
from pymongo.collection import Collection

from pymongo.results import UpdateResult, InsertOneResult

config = dotenv_values(".env")


class MongoConnection:

    def __init__(self, connection_string: str):
        connection_string = config["ATLAS_URI"]

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        self.client = MongoClient(connection_string, tlsCAFile=certifi.where())

        # Create the database for our example (we will use the same database throughout the tutorial
        # client['user_shopping_list']

        reminders_collection = self.client[config['REMINDERS_DB']]
        self.reminders_collection: Collection = reminders_collection[config['REMINDERS_COLLECTION']]

    def ping(self):
        self.client.admin.command('ping')


def create_selection_in_mongo(collection: Collection, selection_dict: dict):
    try:
        updated: InsertOneResult = collection.insert_one(
            selection_dict,
        )
        return updated
    except Exception as e:
        logging.error(e, str(selection_dict)
                      )




