from pymongo import MongoClient
import json
import sys


def connectMongoDB(port):
    global client
    client = MongoClient(f"mongodb://localhost:{port}")

def createDatabase():
    db = client["291db"]
    collections_list = db.list_collection_names()
    if "tweets" in collections_list:
        db["tweets"].drop()
    return db["tweets"]


def fileOpen(filename: str):
    with open(filename, 'r') as jsonFile:
        for line in jsonFile:
            yield json.loads(line)            


def insertData(tweetsdb, jsonData):
    _batch_size = 5000
    dataArray = []
    for document in jsonData:
        dataArray.append(document)
        if len(dataArray) == _batch_size:
            tweetsdb.insert_many(dataArray)
            dataArray = []
    tweetsdb.insert_many(dataArray)


def main():
    # EXAMPLE: python3 project.py 10.json 27017
    arguments = sys.argv
    connectMongoDB(arguments[2])
    tweetsdb = createDatabase()
    jsonData = fileOpen(f"{arguments[1]}")
    insertData(tweetsdb, jsonData)

if __name__ == "__main__":
    main()
