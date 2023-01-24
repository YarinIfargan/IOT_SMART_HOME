import pandas as pd
import sqlite3 

conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("""CREATE TABLE employees1(
    first text,
    last text,
    pay integer)""")

#c.execute("INSERT INTO employees VALUES('Yarin','Ifargan','50000'")
#c.execute("SELECT * FROM employees WHERE last='Ifargan'")

#print(c.fetchone())
conn.commit()
conn.close()