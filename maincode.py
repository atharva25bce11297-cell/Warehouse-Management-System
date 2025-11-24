import sqlite3

def add_good():
    product_id = int(input("Enter product ID : "))
    product_name = input("Enter product name : ")
    quantity = input("Enter quantity : ")
    product_type = input("Enter product type : ")
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO goods (product_id, product_name, quantity, product_type) VALUES (?, ?, ?, ?)",
                   (product_id, product_name, quantity, product_type))
    conn.commit()
    conn.close()
    print("Good added successfully.\n")

def delete_good():
    product_id = int(input("Enter Product ID to delete: "))
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM goods WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()
    print("Good deleted successfully.\n")

def edit_good():
    product_id = int(input("Enter Product ID to edit : "))
    product_name = input("Enter New Product Name : ")
    quantity = input("Enter New Quantity : ")
    product_type = input("Enter New Product Type : ")
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE goods SET product_name=?, quantity=?, product_type=? WHERE product_id=?",
                   (product_name, quantity, product_type, product_id))
    conn.commit()
    conn.close()
    print("Good details updated successfully.\n")

def show_good():
    product_id = int(input("Enter Product ID to view: "))
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM goods WHERE product_id = ?", (product_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print(f"Product ID: {result[0]}, Name: {result[1]}, Quantity: {result[2]}, Type: {result[3]}\n")
    else:
        print("Good not found.\n")

def display_all_goods():
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM goods")
    results = cursor.fetchall()
    conn.close()
    if results:
        for result in results:
            print(f"Product ID: {result[0]}, Name: {result[1]}, Quantity: {result[2]}, Type: {result[3]}")
    else:
        print("No goods in the database")
    print()
def main_menu1():
    while True: 
        print(" Warehouse Goods Menu ")
        
        print(" 1. Add Good ")
        
        print(" 2. Delete Good ")
        
        print(" 3. Edit Good Details ")
        
        print(" 4. Show Good by Product ID ")
        
        print(" 5. Display All Goods ")
        
        print(" 6. Exit ")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_good()
        elif choice == "2":
            delete_good()
        elif choice == "3":
            edit_good()
        elif choice == "4":
            show_good()
        elif choice == "5":
            display_all_goods()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")
   
        
   

#goods table ends here 

def add_entry():
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity: "))
    senders_address = input("Enter Sender's Address: ")
    receivers_address = input("Enter Receiver's Address: ")
    arrival_date = input("Enter Arrival Date (YYYY-MM-DD): ")
    delivery_date = input("Enter Delivery Date (YYYY-MM-DD): ")
    batch_no = input("Enter Batch No.: ")
    
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO shipping_date (product_id, quantity, senders_address, receivers_address, arrival_date, delivery_date, batch_no)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (product_id, quantity, senders_address, receivers_address, arrival_date, delivery_date, batch_no))
    conn.commit()
    conn.close()
    print("Entry added successfully.\n")

def delete_entry():
    product_id = int(input("Enter Product ID to delete : "))
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM shipping_date WHERE product_id = ?", (product_id,))
    conn.commit()
    conn.close()
    print("Entry deleted successfully.\n")

def edit_entry():
    product_id = int(input("Enter Product ID to edit: "))
    quantity = int(input("Enter new Quantity: "))
    senders_address = input("Enter new Sender's Address: ")
    receivers_address = input("Enter new Receiver's Address: ")
    arrival_date = input("Enter new Arrival Date (YYYY-MM-DD): ")
    delivery_date = input("Enter new Delivery Date (YYYY-MM-DD): ")
    batch_no = input("Enter new Batch No.: ")
    
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE shipping_date 
        SET quantity=?, senders_address=?, receivers_address=?, arrival_date=?, delivery_date=?, batch_no=?
        WHERE product_id=?
    ''', (quantity, senders_address, receivers_address, arrival_date, delivery_date, batch_no, product_id))
    
    conn.commit()
    conn.close()
    print ("Entry updated successfully.\n")

def show_entry():
    product_id = int(input("Enter Product ID to display: "))
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shipping_date WHERE product_id = ?", (product_id,))
    entry = cursor.fetchone()
    conn.close()
    if entry:
        print (f"\nProduct ID: {entry[0]}\nQuantity: {entry[1]}\nSender's Address: {entry[2]}\nReceiver's Address: {entry[3]}"
              f"\nArrival Date: {entry[4]}\nDelivery Date: {entry[5]}\nBatch No.: {entry[6]}\n")
    else:
        print ("Entry not found.\n")

def display_all_entries():
    conn = sqlite3.connect('data_warehouse.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM shipping_date")
    entries = cursor.fetchall()
    conn.close()
    if entries:
        for entry in entries:
            print(f"Product ID: {entry[0]}, Quantity: {entry[1]}, Sender: {entry[2]}, Receiver: {entry[3]}, "
                  f"Arrival: {entry[4]}, Delivery: {entry[5]}, Batch No.: {entry[6]}")
    else:
        print ("No entries found.")
    print ()

def main_menu2():
    while True:
        print ("Shipping Details Menu")
        
        print ("1. Add Entry")
        
        print ("2. Delete Entry")
        
        print ("3. Edit Entry")
        
        print ("4. Show Entry by Product ID")
        
        print ("5. Display All Entries")
        
        print ("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_entry()
        elif choice == "2":
            delete_entry()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            show_entry()
        elif choice == "5":
            display_all_entries()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.\n")
ans='y'
while ans in 'Yy':
    print(' 1.manage goods\n 2.manage entries\n 3.exit')
    ans1=int(input('please input what function you want to perform'))
    if ans1==1:
        main_menu1()
    elif ans1==2:
        main_menu2()
    elif ans1==3:
        exit()
    else:
        print('enter a valid option')
        








