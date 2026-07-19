import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()


client = MongoClient(
    os.getenv("MONGO_URI")
)


database = client["nidana_ai"]


reports_collection = database["reports"]