
import mysql.connector
try:
    db = mysql.connector.connect(
        user='root',
        password='password',
        host='127.0.0.1',
        db="plants"
        )

    cursor = db.cursor()
    #cursor.execute("CREATE DATABASE plants")
    #cursor.execute('SHOW DATABASES')

    #with db.cursor() as cursor:
    ''' 
    insert_query = "INSERT INTO plants.customers (customerNumber, customerName, phone, address) VALUES (1, 'Aram', '077-777777', 'Yerevan'),(2, 'Ashot', '077-677777', 'Yerevan')," \
                   "(3, 'Ara', '055-107777', 'Yerevan'), (4, 'Armen', '099-777771', 'Yerevan')," \
                   "(5, 'Gurgen', '055-977777', 'Yerevan'), (6, 'Abraham', '099-777772', 'Vanadzor')," \
                   "(7, 'Lilit', '055-877777', 'Abovyan'), (8, 'Elen', '099-777773', 'Yerevan')," \
                   "(9, 'Narek', '055-677777', 'Artashat'), (10, 'Meri', '099-777774', 'Yerevan')," \
                   "(11, 'Varjuhi', '055-577777', 'Yerevan'), (12, 'Vahram', '099-777775', 'Yerevan')," \
                   "(13, 'Aramayis', '055-477777', 'Tashir'), (14, 'John', '099-777776', 'Vanadzor')," \
                   "(15, 'Vazgen', '055-377777', 'Yerevan'), (16, 'Roni', '099-777777', 'Yerevan')," \
                   "(17, 'Poghos', '055-277777', 'Tashir'), (18, 'Albert', '099-777778', 'Vanadzor')," \
                   "(19, 'Mariam', '055-177777', 'Yerevan'), (20, 'Grig', '099-777779', 'Yerevan')," \
                   "(21, 'Ani', '055-777714', 'Ashtarak'), (22, 'Artak', '099-777710', 'Yerevan')," \
                   "(23, 'Arpine', '055-777713', 'Yerevan'), (24, 'Anna', '099-777711', 'Yerevan'),(25, 'Ando', '055-777712', 'Yerevan');"
                   

    cursor.execute(insert_query) 

  
    insert_query = "INSERT INTO plants.orders (orderNumber, orderDate, status, customerNumber) VALUES (0001, '12.12.21', 'done', 1),(0002, '10.12.21', 'done', 2)," \
                   "(0003, '1.12.21', 'done', 3), (0004, '10.10.20', 'in progres', 4)," \
                   "(0005, '2.12.19', 'done', 5), (0006, '10.2.20', 'done', 6)," \
                   "(0007, '3.12.21', 'done', 15), (0008, '10.3.21', 'done', 7)," \
                   "(0009, '4.12.21', 'in progres', 16), (0010, '10.4.21', 'done', 8)," \
                   "(0011, '5.12.21', 'in progres', 17), (0012, '10.5.21', 'done', 9)," \
                   "(0013, '6.12.21', 'in progres', 18), (0014, '10.6.20', 'in progres', 10)," \
                   "(0015, '7.12.19', 'done', 19), (0016, '10.7.20', 'done', 11)," \
                   "(0017, '8.12.21', 'done', 20), (0018, '10.8.21', 'done', 12)," \
                   "(0019, '9.12.21', 'in progres', 21), (0020, '10.9.21', 'done', 13)," \
                   "(0021, '10.1.21', 'done', 22), (0022, '10.10.21', 'in progres', 14)," \
                   "(0023, '7.10.19', 'in progres', 23), (0024, '1.12.19', 'in progres', 24)," \
                   "(0025, '8.9.21', 'done', 2), (0026, '1.5.19', 'done', 25)," \
                   "(0027, '9.8.21', 'in progres', 8), (0028, '3.10.19', 'done', 10)," \
                   "(0029, '10.8.21', 'done', 20), (0030, '10.1.19', 'done', 10);"
    
    insert_query = "INSERT INTO plants.employees (employeeNumber, lastName, firstName, email, officeCode, jobTitle) VALUES (1, 'Babayan', 'Armenak', 'armBabnik@mail.ru', 111, 'consultant'),"  \
                       "(2, 'Ashot', 'Hambarcumyan', 'asham@mail.ru', 111, 'consultant')," \
                       "(3, 'Aramyan', 'Hamlet', 'arHam@mail.ru', 111, 'consultant')," \
                       "(4, 'Gevorgyan', 'Ara', 'argev@mail.ru', 111, 'manager')," \
                       "(5,  'Asatryan', 'Narek', 'asNar@gmail.com', 111, 'Director'),"\
                       "(6, 'Ashot', 'Hambarcumyan', 'asham@mail.ru', 222, 'consultant')," \
                       "(7, 'Aramyan', 'Hamlet', 'arHam@mail.ru', 222, 'consultant')," \
                       "(8, 'Gevorgyan', 'Ara', 'argev@mail.ru', 222, 'manager')," \
                       "(9,  'Asatryan', 'Narek', 'asNar@gmail.com', 222, 'Director'),"\
                       "(10,  'Asatryan', 'Narek', 'asNar@gmail.com', 222, 'Director');"
    cursor.execute(insert_query)
    
    insert_query = "INSERT INTO plants.stores (officeCode, phone, city, country) VALUES ('111', '093-11-22-33', 'Yerevan', 'Armenia'), " \
                       "('222', '094-19-20-31', 'Yerevan', 'Armenia');"
    

    insert_query = "INSERT INTO plants.employees (employeeNumber, lastName, firstName, email, officeCode, jobTitle) VALUES (1, 'Babayan', 'Armenak', 'armBabnik@mail.ru', 111, 'consultant')," \
                   "(2, 'Ashot', 'Hambarcumyan', 'asham@mail.ru', 111, 'consultant')," \
                   "(3, 'Aramyan', 'Hamlet', 'arHam@mail.ru', 111, 'consultant')," \
                   "(4, 'Gevorgyan', 'Ara', 'argev@mail.ru', 111, 'manager')," \
                   "(5,  'Asatryan', 'Narek', 'asNar@gmail.com', 111, 'Director')," \
                   "(6, 'Ashot', 'Hambarcumyan', 'asham@mail.ru', 222, 'consultant')," \
                   "(7, 'Aramyan', 'Hamlet', 'arHam@mail.ru', 222, 'consultant')," \
                   "(8, 'Gevorgyan', 'Ara', 'argev@mail.ru', 222, 'manager')," \
                   "(9,  'Asatryan', 'Narek', 'asNar@gmail.com', 222, 'Director')," \
                   "(10,  'Asatryan', 'Abgar', 'abgar@gmail.com', 222, 'manager');"
    
    insert_query = "INSERT INTO plants.plants (productCode, productName, buyPrice, productDescription, productImage) VALUES (1, 'bellflower', 1000, 'flowering', '000debaf87.jpg')," \
                   "(2,  'bellflower', 1100, 'flowering', '0.jpg')," \
                   "(3,  'bellflower', 1200, 'flowering', '0aa2a4ee3f.jpg')," \
                   "(4,  'bellflower', 1000, 'non flowering', '0bb23d8f0a.jpg')," \
                   "(5,  'bellflower', 900, 'non flowering', '0c6e980723.jpg')," \
                   "(6,  'daisy', 2000, 'flowering', '0b130baa02.jpg')," \
                   "(7,  'daisy', 2100, 'flowering', '00d451c5a305ae84fd692fee58d80442.jpg')," \
                   "(8,  'daisy', 2000, 'flowering', '0.jpg')," \
                   "(9,  'daisy', 2200, 'non flowering', '0b3ece4baa.jpg')," \
                   "(10,  'daisy', 2300, 'non flowering', '0a64d44c9d.jpg')," \
                   "(11,  'dandelion', 1500, 'flowering', '00d8e4e02d6cafa2e9d3733191ec3e3a.jpg')," \
                   "(12,  'dandelion', 1600, 'flowering', '0.jpg')," \
                   "(13,  'dandelion', 1600, 'flowering', '0c77f6784b.jpg')," \
                   "(14,  'dandelion', 1400, 'non flowering', '0cc16e27ee.jpg')," \
                   "(15,  'dandelion', 1500, 'non flowering', '0e2e92640d.jpg')," \
                   "(16,  'lotus', 3000, 'flowering', '00f3f4ad78.jpg')," \
                   "(17,  'lotus', 2500, 'flowering', '0ad56fc298.jpg')," \
                   "(18,  'lotus', 2700, 'flowering', '0ae299fb48.jpg')," \
                   "(19,  'lotus', 3000, 'non flowering', '0da8c6d908.jpg')," \
                   "(20,  'lotus', 2500, 'non flowering', '0eb3e19c9f.jpg')," \
                   "(21,  'rose', 4000, 'flowering', '00a6e417f2593e4c42e83f626328fd14.jpg')," \
                   "(22,  'rose', 4200, 'flowering', '00c626db1c.jpg')," \
                   "(23,  'rose', 4100, 'flowering', '00f6e89a2f949f8165d5222955a5a37d.jpg')," \
                   "(24,  'rose', 4000, 'non flowering', '0a09d4dac1.jpg')," \
                   "(25,  'rose', 4100, 'non flowering', '0a63a15074.jpg')," \
                   "(26,  'sunflower', 1200, 'flowering', '00af3df40b.jpg')," \
                   "(27,  'sunflower', 1300, 'flowering', '00af3df40b.jpg')," \
                   "(28,  'sunflower', 1200, 'flowering', '00e6ba5240.jpg')," \
                   "(29,  'sunflower', 1400, 'non flowering', '0.jpg')," \
                   "(30,  'sunflower', 1200, 'non flowering', '0bd9acc427.jpg')," \
                   "(31,  'tulip', 1200, 'non flowering', '0a7edf43655eaa77f28ca8a27d1809c2.jpg')," \
                   "(32,  'tulip', 1200, 'flowering', '0b4c4aa6ae18bf15e9676cdd373e34ec.jpg')," \
                   "(33,  'tulip', 1300, 'flowering', '0b7a242b42967aaf439971dc6420b3fd.jpg')," \
                   "(34,  'tulip', 1200, 'flowering', '0b7d00d6d473c3674962140295360cc7.jpg')," \
                   "(35,  'tulip', 1400, 'non flowering', '0bf0285e4301214604cce39014b37e0e.jpg');"
    
    insert_query = "INSERT INTO plants.orderdetails (orderNumber, productCode, quantityOrdered, priceEach) VALUES (0001, 35, 6, 1400), (0002, 34, 4, 1200)," \
                   "(0003, 33, 3, 1300), (0004, 32, 3, 1200)," \
                   "(0005, 31, 7, 1200), (0006, 30, 2, 1200)," \
                   "(0007, 29, 6, 1400), (0008, 28, 4, 1200)," \
                   "(0010, 27, 9, 1300), (0011, 26, 7, 1200)," \
                   "(0012, 25, 4, 4100), (0013, 24, 4, 4000)," \
                   "(0014, 23, 6, 4100), (0015, 22, 2, 4200)," \
                   "(0016, 21, 3, 4000), (0017, 20, 3, 2500)," \
                   "(0018, 19, 7, 3000), (0019, 18, 2, 2700)," \
                   "(0020, 17, 6, 2500), (0021, 16, 4, 3000)," \
                   "(0022, 15, 1, 1500), (0023, 14, 9, 1400)," \
                   "(0024, 13, 14, 1600), (0025, 12, 11, 1600)," \
                   "(0026, 11, 6, 1500), (0027, 10, 4, 2300)," \
                   "(0028, 9, 14, 2200), (0029, 8, 11, 2000)," \
                   "(0030, 5, 21, 900);"
    cursor.execute(insert_query)
    
    #delete_query = "delete from plants.customers where customerNumber = 9;"
    #cursor.execute(delete_query)
    '''


    def employees_by_key(k):
        cursor.execute("SELECT * FROM employees WHERE employeeNumber = " + k)
        res = cursor.fetchall()
        for x in res:
            print(x)
    db.commit()

    def plants_by_key(PlantKey):
        cursor.execute("SELECT * FROM plants WHERE productCode = " + PlantKey)
        res = cursor.fetchall()
        for x in res:
            print(x)
    # print("Hello World")

    def insertPlants(prodCode, prodName, prodPrice, prodDescr, picPath):

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

    def insertCustomer (CustNumber,CustName, CustPhone, CustAddress, EmpNumber):
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
                insertPlants(prodCode, prodName, prodPrice, prodDescr, picPath)
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
                insertCustomer(CustNumber,CustName, CustPhone, CustAddress, EmpNumber)
        elif (inp == "3"):
            print("1.Search Employee\n2.Search Plants\n")
            inp = input()
            if (inp == "1"):
                print("Enter Employee key")
                EmployeeKey = input()
                employees_by_key(EmployeeKey)
            if (inp == "2"):
                print("Enter Plant key")
                PlantKey = input()
                plants_by_key(PlantKey)

        else:
            print("end of game")
            break

except Exception as ex:
    print('Connection failed...')
    print(ex)