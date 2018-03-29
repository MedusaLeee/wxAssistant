from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db = conn['wx-assistant']
friends = db.friends

friends.save({'name': 'jianxun', 'age': 28})

me = friends.find_one({'name': 'jianxun'})

print(me)

personArr = friends.find()

for i in personArr:
    print(i)
