import pymango
from pymango import MangoClient
c1=MangoClient("mangodb+srv:")
db=c1["test"]
collection=db["traintest"]
post={}
collection.insert_one(post)
