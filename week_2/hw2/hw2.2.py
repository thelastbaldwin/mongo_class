import pymongo

connection = pymongo.MongoClient() #make the connection, defaults to localhost
students = connection.students #get the students database

#check to see that we can get data from the database
#print students.grades.find_one();

#get all homework scores
sorted_grades = students.grades.find({"type": "homework"}).sort([('student_id',pymongo.DESCENDING), ('score',pymongo.ASCENDING)])

#this block will identify the lowest scores
last_id = ''
for grade in sorted_grades:
    student_id = grade["student_id"]
    score = grade["score"]

    if student_id is not last_id:
        #because the scores are sorted lowest to highest, this is the lowest score
        students.grades.remove({"score" : score, "student_id" : student_id}, safe = True)
        print "the lowest grade for student no. {0} was {1} and has been removed".format(student_id, score)
        last_id = student_id



