import sqlite3  # part of std library
import os
from _37_3_employee_class import Employee

os.chdir("D:\Python\sqlite3")
print(os.getcwd())

conn = sqlite3.connect(
    ":memory:"
)  # for testing as db is generated in RAM, generated over and over, completely fresh
# conn = sqlite3.connect('_37_2_employee.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
            )""")


def insert_emp(emp):
    with conn:
        cur.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


def get_emp(lastname):
    cur.execute("SELECT * FROM employees WHERE last = :last", {"last": lastname})
    return cur.fetchall()


def update_pay(emp, pay):
    with conn:
        cur.execute(
            "UPDATE employees SET pay = :pay WHERE first = :first AND last = :last",
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp):
    with conn:
        cur.execute(
            "DELETE FROM employees where first = :first AND last = :last",
            {"first": emp.first, "last": emp.last},
        )


emp_1 = Employee("john", "doe", 80000)
emp_2 = Employee("jane", "doe", 90000)

# cur.execute("""INSERT INTO employees VALUES("corey", "schafer", 50000)""")
# cur.execute("""INSERT INTO employees VALUES("mary", "schafer", 60000)""")

# using string formatting to insert values makes the db prone to sql injection so do not use f-strings or string formatting

# cur.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# cur.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
# conn.commit()

# cur.execute("SELECT * FROM employees WHERE last = ?", ('schafer',)) # returns 'None' if not found
# print(cur.fetchall())

# cur.execute("SELECT * FROM employees WHERE last = :last", {'last': 'doe'}) # returns 'None' if not found
# print(cur.fetchall())

# print(cur.fetchone())


# conn.commit()

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emp("doe")
print(emps)

update_pay(emp_1, 100000)
emps = get_emp("doe")
print(emps)

remove_emp(emp_2)
emps = get_emp("doe")
print(emps)

conn.close()
