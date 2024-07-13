class Employee:
    def __init__(self, name, pay):
        self._name = name
        self._pay = pay
        self._email = f"{name}@gmail.com"

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self._name

    
from Employee import Employee

class Developer(Employee):
    
    def __init__(self, name, pay, prog_lang) :
        self._name= name
        self._pay= pay
        self._prog_lang= prog_lang
        
    def __str__(self) :
        return self._name, self._pay,self._prog_lang
        

from Employee import Employee
class Manager(Employee):

    def __init__(self, name, pay, employees=None):
        super().__init__(name, pay)
        if employees is None:
            self._employees = []
        else:
            self._employees = employees
    
    def add_employee(self, emp):
        if emp not in self._employees:
            self._employees.append(emp)

    def remove_employee(self, emp):
          if emp not in self._employees:
            self._employees.append(emp)

    def __str__(self):
        emp_list = "None" if not self._employees else " ".join(emp.name for emp in self._employees)
        return f"Manager Name :{self._name}\nEmployee List :\n{emp_list}"
    
from Employee import Employee
from Developer import Developer

class Utility :
	@staticmethod
	def print_employees_under_each_manager(manager_list) :
		allocation_list=[]
		for manager in  manager_list:
			allocation_list.append(str(manager))
		return allocation_list

rom Employee import Employee
from Developer import Developer
from Manager import Manager
from Utility import Utility


manager_list = []
manager_list.append(Manager("Arun",80000))
manager_list.append(Manager("Babu",100000))
manager_list.append(Manager("Chandru",60000))
manager_list.append(Manager("Deva",60000))

input_obj_list = []
choice = "yes"
while choice=="yes" :
	print("Menu\n1)Employee\n2)Developer\n")
	choice1 = input("Enter choice\n")
	if choice1 == "1" :
		input_str = input("Enter Employee details in comma separated format\n")
		name, pay = input_str.split(",")
		employee = Employee(name, pay)
		input_obj_list.append(employee)
		mgr_name = input("Enter manager name\n")
		for manager in manager_list :
			if manager.name == mgr_name :
				manager.add_employee(employee)
				
	else :
		input_str = input("Enter Developer details in comma separated format\n")
		name, pay, prog_lang = input_str.split(",")
		developer = Developer(name, pay, prog_lang)
		input_obj_list.append(developer)
		mgr_name = input("Enter manager name\n")
		for manager in manager_list :
			if manager.name == mgr_name :
				manager.add_employee(developer)
	choice = input("Do you want to continue? Type yes/no\n")

print("\nManager and Employee Allocation List")	
Utility.print_employees_under_each_manager(manager_list)
print("\n")

