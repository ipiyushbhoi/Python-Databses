import sqlite3
import os
from employee import Employee

conn = sqlite3.connect('employee.db')

emp1 = Employee('Jason', 420, 'CSE', 42000)
employee_list = [('Bill', 421, 'CSE', 42000), 
                 ('Ray', 422, 'IT', 35000),
                 ('Kate', 423, 'ECE', 30000),
                 ('Shawn', 424, 'EEE', 28000),
                 ('John', 425, 'MECH', 30000)]

cursor = conn.cursor()

# Supported datatypes
'''
NULL    : The value is a NULL value.
INTEGER : The value is a signed integer, stored in 1, 2, 3, 4, 6, 
          or 8 bytes depending on the magnitude of the value.
REAL    : The value is a floating point value, stored 
          as an 8-byte IEEE floating point number.
TEXT    : The value is a text string, stored using the database
          encoding (UTF-8, UTF-16BE or UTF-16LE).
BLOB    : The value is a blob of data, stored exactly as it was input.
'''
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


cursor.execute(INSERT, (emp1.emp_name, emp1.emp_id,
                        emp1.emp_department,
                        emp1.emp_salary))
conn.commit()

cursor.execute(SELECT)
conn.commit()
print(cursor.fetchall())

cursor.executemany(INSERT, employee_list)
conn.commit()


cursor.execute(SELECT)
conn.commit()
print(cursor.fetchall())

conn.close()
