#44. Create a table cust_info as sr_no, name, DOB, mobile. Ask user to enter the information from python code. Validate all fields and after validation insert records in the table.

import mysql.connector  
import mysql.connector
import re
from datetime import datetime


conn = mysql.connector.connect(
    host="localhost",
    user="root",)

cursor = conn.cursor()


while True:
    sr_no = input("Enter Serial Number: ")
    if sr_no.isdigit():
        sr_no = int(sr_no)
        break
    else:
        print("Invalid! Serial number must be numeric.")


while True:
    name = input("Enter Name: ")
    if name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid! Name must contain only letters.")


while True:
    dob = input("Enter DOB (YYYY-MM-DD): ")
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        break
    except:
        print("Invalid DOB format! Use YYYY-MM-DD")


while True:
    mobile = input("Enter Mobile Number: ")
    if re.fullmatch(r"[0-9]{10}", mobile):
        break
    else:
        print("Invalid! Mobile must be 10 digits.")



query = "INSERT INTO cust_info (sr_no, name, DOB, mobile) VALUES (%s, %s, %s, %s)"
values = (sr_no, name, dob, mobile)

cursor.execute(query, values)
conn.commit()

print("Record inserted successfully!")

cursor.close()
conn.close()
