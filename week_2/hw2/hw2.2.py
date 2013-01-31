import pymongo

connection = pymongo.MongoClient() #make the connection, defaults to localhost
students = connection.students #get the students database

print students.grades.find_one();



