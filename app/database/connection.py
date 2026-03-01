from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import certifi

uri = "mongodb+srv://explain_my_code:1234@cluster0.ndtjjp9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'), tlsAllowInvalidCertificates=True, tlsCAFile=certifi.where())

# Select Database
database = client["explain_my_code_db"]

# Collections
users_collection = database["users"]
explanations_collection = database["explanations"]

try:
    client.admin.command('ping')
    print("MongoDB Connected Successfully ✅")
except Exception as e:
    print("Connection Failed ", e)