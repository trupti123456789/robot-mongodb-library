import pymongo
from bson.objectid import ObjectId

def Update(con,id,data):
    try:
        db=pymongo.MongoClient("mongodb://"+con["username"]+":"+con["password"]+"@"+con["host"]+":"+con["port"])[con["database"]][con["collection"]] 
        try:
            _id=ObjectId(id)
        except:
            _id=id
        if db.update_one({"_id":_id},{ "$set": data}).modified_count !=0:
            return "UPDATED SUCCESS"
        return "DATA NOT FOUND"
    except:
        return "UPDATED ERROR"