students = [

    {"name": "Alice", "math": 85, "science": 90, "english": 78},

    {"name": "Bob", "math": 70, "science": 88, "english": 82},

    {"name": "Charlie", "math": 92, "science": 87, "english": 85},

]


sum = []
for i in students:
        avarage = (i["math"] + i["science"] + i["english"])/3
        a= {"name":i["name"],"avarage":avarage}
        sum.append(a)
print(sum)
        


#    avg = {}
#    sum =  i("math")+ i("science") + i("english")/3
#    avg.insert(sum)
   

#    stu = {}
#    stu.insert(i("name"), i(avg))
#    print(stu)


# Midhusha Suresh
# 18:45
# You are given a list of dictionaries. Each dictionary represents a student and their grades in various subjects.

# students = [

#     {"name": "Alice", "math": 85, "science": 90, "english": 78},

#     {"name": "Bob", "math": 70, "science": 88, "english": 82},

#     {"name": "Charlie", "math": 92, "science": 87, "english": 85},

# ]

# 1. Loop through the list of students.
# 2. For each student:

# Calculate the average grade.
# Store the result in a new dictionary in the format:
# {"name": "Alice", "average": 84.33}

# 3. Print out the new list of dictionaries containing each student's name and average grade.