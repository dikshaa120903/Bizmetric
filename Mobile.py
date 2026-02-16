import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()


class User:
    
    def __init__(self, mobile, passkey):
        self.mobile = mobile
        self.passkey = passkey
        self.uid = None
    
  
    def sign_up(self):
        query = "INSERT INTO user (mobile, passkey, date) VALUES (%s, %s, %s)"
        values = (self.mobile, self.passkey, date.today())
        cursor.execute(query, values)
        conn.commit()
        print("Signup Successful ")

    def sign_in(self):
        query = "SELECT uid FROM user WHERE mobile=%s AND passkey=%s"
        cursor.execute(query, (self.mobile, self.passkey))
        result = cursor.fetchone()
        
        if result:
            self.uid = result[0]
            print("Login Successful ")
            return True
        else:
            print("Invalid Credentials")
            return False
    
    def view_products(self):
        cursor.execute("SELECT * FROM product")
        products = cursor.fetchall()
        
        print("\nAvailable Products:")
        for p in products:
            print(f"PID: {p[0]}, Name: {p[1]}")
    
    def place_order(self, pid):
        if self.uid:
            query = "INSERT INTO orders (uid, pid) VALUES (%s, %s)"
            cursor.execute(query, (self.uid, pid))
            conn.commit()
            print("Order Placed Successfully ✅")
        else:
            print("Please login first")
    
    def view_orders(self):
        if self.uid:
            query = """
            SELECT o.oid, p.pname
            FROM orders o
            JOIN product p ON o.pid = p.pid
            WHERE o.uid = %s
            """
            cursor.execute(query, (self.uid,))
            orders = cursor.fetchall()
            
            print("\nYour Orders:")
            for o in orders:
                print(f"Order ID: {o[0]}, Product: {o[1]}")
        else:
            print("Please login first")


mobile = input("Enter Mobile: ")
password = input("Enter Password: ")

user1 = User(mobile, password)

choice = input("1.Sign Up  2.Sign In : ")

if choice == "1":
    user1.sign_up()

elif choice == "2":
    if user1.sign_in():
        user1.view_products()
        pid = int(input("Enter Product ID to place order: "))
        user1.place_order(pid)
        user1.view_orders()

cursor.close()
conn.close()
