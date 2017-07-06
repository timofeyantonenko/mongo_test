"""
1) install mongoDB to Ubuntu;
2) add additional settings (unmask, etc)
2) install pymongo with pip;
"""
import datetime
import random

from pymongo import MongoClient

DATABASE = "timofey-db"
COLLECTION = 'first-collection'

random_chars = "abcdefghijklmopqrstuvwxyzАБВГДЕЖЗ"

selectors_range = [10000, 10010]
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
    collection.create_index("name")
    posts = make_select(collection,
                        {"name": {"$regex": "А."},
                         "number": {"$gt": selectors_range[0], "$lt": selectors_range[1]},
                         })
    # posts = fetch_all(collection)
    for post in posts:
        print(post)


if __name__ == '__main__':
    main()
