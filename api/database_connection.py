from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

uri = os.getenv('DB_URL')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def test():
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

#name, gender, orientation, gps (longitude and latitude)

def add_data():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.get_database("sample_mflix")
    collection = db["hi"]
    collection.create_index([('name', 1)], unique=True)


    document = {
        'name': 'Annie Vu',
        'gender' : 'male'
    }

    filter_criteria = {'name': 'Annie Vu'}
    update_criteria = {'$set': document}

    result = collection.update_one(filter_criteria, update_criteria, upsert = True)

