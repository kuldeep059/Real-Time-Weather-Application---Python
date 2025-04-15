from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['weather_db']
collection = db['weather_data']

# Drop the conflicting index
collection.drop_index("timestamp_1")
print("Dropped existing index 'timestamp_1'.")

# Recreate it with 7-day TTL
collection.create_index(
    [('timestamp', 1)],
    expireAfterSeconds=604800
)
print("Created new TTL index on 'timestamp' with 7-day expiration.")
