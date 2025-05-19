from math import*

def enrollment_stats():
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]

    students=[]
    tuition=[]

    sum_cnt_students=0
    sum_tuition=0
    for i in range(len(universities)):
        sum_cnt_students+=universities[i][1]
        sum_tuition+=universities[i][2]
        students.append(universities[i][1])
        tuition.append(universities[i][2])
    print("Total students:", sum_cnt_students, "\nTotal tuition: $", sum_tuition)

    students.sort()
    tuition.sort()

    print("\nStudent mean:", round(sum_cnt_students/len(students),2), "\nStudent median:", students[len(students)//2])

    print("\nTuition mean: $", round(sum_tuition/len(tuition),2), "\nTuition median: $", tuition[len(tuition)//2])
    

print("*"*30)
enrollment_stats()
print("*"*30)