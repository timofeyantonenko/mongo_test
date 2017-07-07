import os
import pandas as pd
import pandas_access as mdb
from pymongo import MongoClient

from mongo_connector import insert_to_mongo, DATABASE, COLLECTION

DB_NAME = "Борей.mdb"


def read_tables(db_path):
    result = []
    for tbl in mdb.list_tables(db_path, encoding="utf-8"):
        result.append(tbl)
    return result


def save_tables(tables):
    for table in tables:
        os.system("mdb-export {0} {1} > {1}.csv".format(DB_NAME, table))


def merge_orders():
    orders_df = pd.read_csv("Заказано.csv")
    products_df = pd.read_csv("Товары.csv")
    types_df = pd.read_csv("Типы.csv").drop('Изображение', 1)
    prod_and_types = pd.merge(products_df, types_df, on="КодТипа")
    prod_and_types_and_orders = pd.merge(orders_df, prod_and_types, on="КодТовара")
    return prod_and_types_and_orders.T.to_dict().values()


def main():
    # tables = read_tables(DB_NAME)
    # save_tables(tables)
    client = MongoClient('localhost', 27017)
    db = client[DATABASE]
    collection = db[COLLECTION]
    collection.create_index("Описание")
    orders = merge_orders()
    insert_to_mongo(collection, list(orders))


if __name__ == '__main__':
    main()
