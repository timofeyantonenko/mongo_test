"""
1) install mongoDB to Ubuntu;
2) add additional settings (unmask, etc)
2) install pymongo with pip;
"""
import datetime

from pymongo import MongoClient


def testMongo():
    client = MongoClient('localhost', 27017)
    db = client['timofey-db']
    collection = db['first-collection']
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    # post_id = collection.insert_one(post).inserted_id
    # print(post_id)
    print(db.collection_names(include_system_collections=False))
    print(collection.find_one({"text": "My first blog post!"}))


def main():
    testMongo()


if __name__ == '__main__':
    main()
