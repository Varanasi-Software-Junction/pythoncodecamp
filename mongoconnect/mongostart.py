import json
import urllib.parse
import pymongo
from pymongo import MongoClient

"""
client = pymongo.MongoClient("mongodb+srv://vsj:<password>@cluster0.kxlnv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

"""


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    pwd = urllib.parse.quote_plus("@TTa9S*TpKA7%PP")
    # mongodb: // mongodb0.example.com: 27017

    client = pymongo.MongoClient("mongodb://localhost:27017/vsj")

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['vsj']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()
    print(dbname)
    collection_name = dbname["vsj"]

    item_1 = {
        "_id": "10091",
        "teamname": "Tie"
    }
# collection_name.insert_many([item_1])
# result = collection_name.find({"teamname": "Tie"})
result = collection_name.find()
print(result)
a = list(result)
print(a)
a = a[0]
js = json.dumps(a)
print(js)
js = json.loads(js)
print(js)
collection_name.update_many(
    {"teamname": "Tie"},
    {
        "$set": {"teamname": "True"}
    }
)

collection_name.delete_many({"_id": "U1IT00001"})