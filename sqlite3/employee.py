class Employee:

    def __init__(self, emp_name, emp_id, emp_department, emp_salary):
        """To initialize employee data"""
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_department = emp_department
        self.emp_salary = emp_salary

    def print_emp(self):
        """To print employee data"""
        print(self.emp_name)
        print(self.emp_id)
        print(self.emp_department)
        print(self.emp_salary)

# if __name__ == "__main__":

#     emp_obj = Employee('Jason', '420', 'CSE', '42000')
#     emp_obj.print_emp()