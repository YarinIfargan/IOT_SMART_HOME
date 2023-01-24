import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')
c=conn.cursor()

#create db from scratch
#conn = sqlite3.connect(':memory:')
#c=conn.cursor()

#creating a table in the db
#c.execute("""CREATE TABLE employees(
#        first text,
#       last text,
#      pay integer
#     )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp.first,'last':emp.last,'pay':emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute ("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = : last""",
                    {'first': emp.first, 'last': emp. last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute ("DELETE from employees WHERE first = :first AND last = :last",
                 {'first': emp. first, 'last': emp. last})


#creating new instances of employees using Employee class
emp_1=Employee('Yaron','Mashmur',40500) 
emp_2=Employee('Yoyo','Gozaya',2000)

#using the methods for working with the db
insert_emp(emp_1)
insert_emp(emp_2)
emps = get_emps_by_name('Smith')
print(emps)
update_pay(emp_1,90000)
remove_emp(emp_2)


"""
#adding row into the table
c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first,emp_1.last,emp_1.pay))
conn.commit()
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})
conn.commit()


#selecting row from the table
c.execute("SELECT * FROM employees WHERE last='Smith'")
print(c.fetchall())
c.execute("SELECT * FROM employees WHERE first=?", ('Yarin',))
print(c.fetchall())
c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Benin'})
print(c.fetchall())

conn.commit()
"""
conn.close()