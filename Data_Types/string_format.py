student_name = input('Enter your Name  : ')
employee_id = int(input('Enter your Employee ID : '))
print(f'Student Name : {student_name}\nEmployee ID : {employee_id}')
print(f'Student Name : {student_name.title()}\nEmployee ID : {employee_id}')
print(f'Student Name : {student_name.upper()}\nEmployee ID : {employee_id}')
print(f'Student Name : {student_name.lower()}\nEmployee ID : {employee_id}')

#format method 
print('Student Name : {} \nEmployee ID :{}'.format(student_name,employee_id))
print('Student Name : {} \nEmployee ID :{}'.format(employee_id,student_name))
