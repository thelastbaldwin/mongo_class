#hw3.1.py
#must have a fresh dataset from students.js file for this to be effective

import pymongo

connection = pymongo.MongoClient() #make the connection, defaults to localhost
school = connection.school #get the students database

#check to see that we can get data from the database before moving on
#print school.students.find_one();

def getLowestHWIndex(scores):
    hwScores = {}

    for i in range(0, len(scores)):
        if scores[i]["type"] == "homework": 
            hwScores[i] = scores[i]["score"]

    lowestIndex = 0
    lowestValue = 101 #higher than the maximum score, so every value will be < this

    for key in hwScores:
        if hwScores[key] < lowestValue:
            lowestValue = hwScores[key]
            lowestIndex = key

    return lowestIndex


#get all the students
all_students = school.students.find()

for student in all_students:
    scores = student["scores"]

    print "Student {0} scores are: ".format(student["_id"])

    for score in scores:
        print score
    
    print "The lowest homework score index is: ", getLowestHWIndex(scores)
    del scores[getLowestHWIndex(scores)]

    # print "Student {0} scores with lowest homework removed are are: ".format(student["_id"])
    # for score in scores:
    #     print score

    print "Updating student scores with lowest score removed"
    school.students.update({"_id" : student["_id"]}, {"$set": {"scores" : scores}})