n = int(input("Enter Employee Details"))
employee = {}

for i in range(n):
    name = input("Enter Emplyee Name")
    salary = input("Enter Employee Salary")
    employee[name] = salary
# print(employee.get(salary))
print("One line Code Key value: ", list(employee.keys()))
  

# while True:
#     name = input("Enter Employee Name")
#     salary = employee.get(name, -1)
#     if salary == -1:
#         print("Employ doesn't Exit")
#     else:
#         print("The salary of employee {} is :- ".format(name),salary)
#     choice = input("Do you want to continue[Yes|No]")
#     if choice == "No":
#         break