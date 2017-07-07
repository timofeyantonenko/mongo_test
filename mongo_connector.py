"""
1) install mongoDB to Ubuntu;
2) add additional settings (unmask, etc)
2) install pymongo with pip;
"""
import datetime
import random
import json

from bson import json_util
from pymongo import MongoClient
from bson.json_util import dumps

DATABASE = "timofey-db"
COLLECTION = 'Orders'

random_chars = "abcdefghijklmopqrstuvwxyzАБВГДЕЖЗ"

selectors_range = [10300, 10510]
selector_first_letter = "А"


def insert_to_mongo(collection, documents):
    result = collection.insert_many(documents)
    return result


def generate_docs(count):
    result = []
    for _ in range(count):
        result.append({
            "name": "{}{}".format(random.choice(random_chars), random.choice(random_chars)),
            "number": random.randint(9999, 10020)
        })
    return result


def base_mongo():
    client = MongoClient('localhost', 27017)
    db = client[DATABASE]
    collection = db[COLLECTION]
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    post_id = collection.insert_one(post).inserted_id


def generate_and_insert(mongo_client):
    db = mongo_client[DATABASE]
    collection = db[COLLECTION]
    posts_to_insert = generate_docs(1000)
    posts_ids = insert_to_mongo(collection=collection, documents=posts_to_insert)
    print(posts_ids)


def fetch_all(collection):
    return collection.find()


def make_select(collection, query):
    return collection.find(query)


def main():
    client = MongoClient('localhost', 27017)
    db = client[DATABASE]
    collection = db[COLLECTION]
    # posts = make_select(collection,
    #                     {
    #                         "Описание": {"$regex": "А."},
    #                         "КодЗаказа": {"$gt": selectors_range[0], "$lt": selectors_range[1]},
    #                     })
    posts = fetch_all(collection)
    result = {"result": []}
    for post in posts:
        result["result"].append(post)
    page_sanitized = json.loads(json_util.dumps(result))
    with open('result.json', 'w') as fp:
        json.dump(page_sanitized, fp, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
