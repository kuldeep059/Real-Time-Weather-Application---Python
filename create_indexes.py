from pymongo import MongoClient, ASCENDING, DESCENDING
from dotenv import load_dotenv
import os

# Load environment variables from .env (useful for production/deployment)
load_dotenv()

# Use environment variable if provided, else fallback to localhost (for local dev)
mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
db_name = os.environ.get("DB_NAME", "weather_db")

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client[db_name]
collection = db['weather_data']

# Drop any existing TTL index on timestamp (optional cleanup)
try:
    collection.drop_index("timestamp_1")
    print("⚠️ Dropped existing TTL index on 'timestamp'")
except Exception as e:
    print(f"ℹ️ No existing TTL index to drop: {e}")

# Create required indexes
collection.create_index([('location', ASCENDING)])
collection.create_index([('timestamp', DESCENDING)])

# Create TTL index on timestamp field for 7 days (604800 seconds)
collection.create_index(
    [('timestamp', ASCENDING)],
    expireAfterSeconds=604800
)

print("✅ Indexes created successfully.")
