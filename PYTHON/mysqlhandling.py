import mysql.connector as mysql

def keyboardInput(datatype, caption, errorMessage, defaultValue=None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if (value.strip() == ""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

def doMenu(connection):
    choice = -1
    while (choice != 0):
        print("--------------")
        print("| 0 - Exit   |")
        print("| 1 - List   |")
        print("| 2 - Add    |")
        print("| 3 - Edit   |")
        print("| 4 - Delete |")
        print("--------------")
        choice = keyboardInput(int, "Choice [0, 1, 2, 3, 4]: ", "Choice must be Integer")
        if (choice == 0):
            print("Thank you for using our system")
            break
        elif (choice == 1):
            printProduct(connection)
        elif (choice == 2):
            addProduct(connection)
        elif (choice == 3):
            editProduct(connection)
        elif (choice == 4):
            deleteProduct(connection)

def dbConnect():
    connection = mysql.connect(
        host="localhost", user="root", password="", database="peneraju")
    return connection

def addProduct(connection):
    try:
        product = keyboardInput(str, "Product: ", "Product must be String")
        description = keyboardInput(str, "Description:", "Description must be String")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be Integer")
        price = keyboardInput(float, "Price: ", "Price must be Float")
        SQL = f"""INSERT INTO products (name, description, quantity, price) VALUES 
                ('{product}', '{description}', {quantity}, {price})"""
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()
    except Exception as e:
        print("Something went wrong when we append the product:", e)

def printProduct(connection):
    SQL = f"SELECT id, name, description, quantity, price FROM products"
    cursor = connection.cursor()
    cursor.execute(SQL)
    print("=" * 110)
    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':>20s}|{'Price':>20s}")
    print("=" * 110)
    for id, name, description, quantity, price in cursor:
        print(f"{id:<6d}|{name:20s}|{description:40s}|{quantity:20d}|{price:20.2f}")
    print("=" * 110)

def editProduct(connection):
    try:
        id = keyboardInput(int, "Please keyin the Product Id: ", "Index must be Integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()
    except:
        print("Product for this ID does not exists")
    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str, "Are you sure you want to edit this product (y/n) ?", "Response must be string")
        if (confirm == 'y'):
            newproduct = keyboardInput(str, f"Product [{name}]: ", "Product must be String", name)
            newdescription = keyboardInput(str, f"Description [{description}]: ", "Product must be String", description)
            newquantity = keyboardInput(int, f"Quantity [{quantity}]: ", "Quantity must be Integer", quantity)
            newprice = keyboardInput(float, f"Price [{price}]: ", "Price must be Float", price)
            SQL = f"""UPDATE products SET name='{newproduct}', description='{newdescription}',
                        quantity={newquantity}, price={newprice} WHERE id = {id}"""
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

def deleteProduct(filename):
    try:
        id = keyboardInput(int, "Please keyin the Product Id: ", "Index must be Integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()
    except:
        print("Product for this ID does not exists")
    else:
        print(f"Product: {name}\nDescription: {description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str, "Are you sure you want to delete this product (y/n) ?", "Response must be string")
        if (confirm == 'y'):
            SQL = f"""DELETE FROM products WHERE id = {id}"""
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

connection = dbConnect()
doMenu(connection)