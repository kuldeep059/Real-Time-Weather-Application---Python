from pymongo import MongoClient, ASCENDING, DESCENDING
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient("mongodb://localhost:27017/")
db = client['weather_db']
collection = db['weather_data']

# Create indexes
collection.create_index([('location', ASCENDING)])
collection.create_index([('timestamp', DESCENDING)])
collection.create_index(
    [('timestamp', ASCENDING)],
    expireAfterSeconds=604800  # 7 days
)

print("✅ Indexes created.")
