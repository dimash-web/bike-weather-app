import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

mongodb_uri = os.getenv("MONGO_URI")

client = pymongo.MongoClient(mongodb_uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client.close()