import pymongo

connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017, username="yx2017", password="kTgsDap9", authSource="yx2017")

collection = connection["yx2017"]["listings"]

docs = collection.find({ "beds": { "$gt": 2 }, "neighbourhood_group_cleansed": "", "review_scores_rating": {"$ne": ""} }, { "_id": 0, "name": 1, "beds": 1, "review_scores_rating": 1, "price": 1 }).sort("review_scores_rating", -1)

for doc in docs:
    print(doc)
