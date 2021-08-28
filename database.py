import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

emp1 = Employee('Jason', '420', 'CSE', '42000')

cursor = conn.cursor()

# Create table employee
CREATE = """CREATE TABLE employee(
            name TEXT,
            id INT,
            department TEXT,
            salary INT)
        """
# Insert values into table
INSERT = "INSERT INTO employee VALUES (?, ?, ?, ?)"

# Show values from table
SELECT = "SELECT * FROM employee"

cursor.execute(CREATE)
conn.commit()
print(cursor.fetchall())

cursor.execute(INSERT, (emp1.emp_name, emp1.emp_id,
                        emp1.emp_department,
                        emp1.emp_salary))
conn.commit()
print(cursor.fetchall())

cursor.execute(SELECT)
conn.commit()
print(cursor.fetchall())
