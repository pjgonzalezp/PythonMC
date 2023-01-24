x = 10
y = '10'
z = 10.1

sum1 = x + x
sum2 = y + y

#print(sum1, sum2)
#print("X:", type(x))
#print("Y:", type(y))
#print("Z:", type(z))

student_grades = [9.1, 8.8, 7.5]
student = [9, "Hello", [1,2,4.33]]
print(student)
print(student * 3) # lista repetida 3 veces
# print(student + 3)  # genera error
print(student + student) # lista repetida 2 veces


students2 = list(range(0,11))
print(students2)

students3 = list(range(0,11,2)) # lista de 0 a 10 de dos en dos
print(students3)

mysum = sum(student_grades)
lenght = len(student_grades)
mean = mysum / lenght
print(mean)
