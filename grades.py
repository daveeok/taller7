import pprint

grades = {
 "Carlos": [4.0, 3.5, 4.5] ,
 "Mariana": [4.8, 5.0, 4.7] ,
 "Andres": [3.0, 2.8, 3.5]
}

def average(name):
    student = grades.get(name)
    average = sum(student) / len(student)
    return average


studentA = "Carlos"
studentB = "Mariana"
studentC = "Andres"

averageA = average(studentA)
averageB = average(studentB)
averageC = average(studentC)

print(f"""
------------ Promedios ------------
{studentA}: {averageA}
{studentB}: {averageB}
{studentC}: {averageC}
-----------------------------------
""")

print("Nota agregada a carlos")
carlos = grades.get("Carlos")
carlos.append(4.0)

print(carlos)

print("Mejor promedio")
averages = [averageA, averageB, averageC]
pos = [studentA, studentB, studentC]
maxAverage = max(averages)
print(f"{pos[averages.index(maxAverage)]}: {maxAverage}")
 



