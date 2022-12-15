import db as db
import mysql.connector
from mysql.connector import cursor

class Application:
    def __init__(self):
        self.__init__()

    db = mysql.connector.connect(
        user='root',
        password='password',
        host='127.0.0.1',
        db="plants"
    )
    cursor = db.cursor()

    def employees_by_key(self, k):
        cursor.execute("SELECT * FROM employees WHERE employeeNumber = " + k)
        res = cursor.fetchall()
        for x in res:
            print(x)

    db.commit()

    def plants_by_key(self, PlantKey):
        cursor.execute("SELECT * FROM plants WHERE productCode = " + PlantKey)
        res = cursor.fetchall()
        for x in res:
            print(x)

    def insertPlants(self, prodCode, prodName, prodPrice, prodDescr, picPath):

        insert_query = (
            "INSERT INTO plants.plants (productCode, productName, buyPrice, productDescription, productImage)"
            "VALUES (%s, %s, %s, %s, %s)"
        )
        data = (int(prodCode), prodName, int(prodPrice), prodDescr, picPath)

        try:
            # Executing the SQL command
            cursor.execute(insert_query, data)

            # Commit your changes in the database
            db.commit()

        except:
            # Rolling back in case of error
            db.rollback()

        print("Data inserted\n")

    def insertCustomer(self, CustNumber, CustName, CustPhone, CustAddress, EmpNumber):
        insert_query = (
            "INSERT INTO plants.customers (customerNumber, customerName, phone, address, employeeNumber)"
            "VALUES (%s, %s, %s, %s, %s)"
        )
        data = (int(CustNumber), CustName, CustPhone, CustAddress, int(EmpNumber))

        try:
            # Executing the SQL command
            cursor.execute(insert_query, data)

            # Commit your changes in the database
            db.commit()

        except:
            # Rolling back in case of error
            db.rollback()

        print("Data inserted\n")
    def run(self):
        while (True):
            print("***Select option***\n1.Insert \n2.Erase \n3.Filtered search\n")
            inp = input()
            if (inp == "1"):
                print("1.Plants\n2.Customer\n")
                inp = input()
                if (inp == "1"):
                    print("Product Code  ")
                    prodCode = input()
                    print("Product Name  ")
                    prodName = input()
                    print("Price  ")
                    prodPrice = input()
                    print("Product Dectription  ")
                    prodDescr = input()
                    print("ImagePath ")
                    picPath = input()
                    self.insertPlants(prodCode, prodName, prodPrice, prodDescr, picPath)
                if (inp == "2"):
                    print("Customer Number ")
                    CustNumber = input()
                    print("Customer Name ")
                    CustName = input()
                    print("Customer phone ")
                    CustPhone = input()
                    print("Customer address ")
                    CustAddress = input()
                    print("Employee number ")
                    EmpNumber = input()
                    self.insertCustomer(CustNumber, CustName, CustPhone, CustAddress, EmpNumber)
            elif (inp == "3"):
                print("1.Search Employee\n2.Search Plants\n")
                inp = input()
                if (inp == "1"):
                    print("Enter Employee key")
                    EmployeeKey = input()
                    self.employees_by_key(EmployeeKey)
                if (inp == "2"):
                    print("Enter Plant key")
                    PlantKey = input()
                    self.plants_by_key(PlantKey)

            else:
                break


oApp = Application()
oApp.run()

