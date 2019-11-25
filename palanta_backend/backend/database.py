import pymongo


def create_client():
    return pymongo.MongoClient()


def get_palanta_db():
    return create_client().palanta
