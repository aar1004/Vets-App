from session14a import DBHelper
from session14 import Customer
from tabulate import tabulate
from session15 import Pet
from session17 import Consultation


def pets_menu():
    db = DBHelper()

    message = """
        >>Pets Menu<<
       1: Add Pet
       2: Update Pet
       3: Delete Pet
       4: View All Pets
       5: View Customers Pets
       0: Quit
       """
    print(message)
    choice = int(input("Enter Your Choice: "))

    pet = Pet()
    customer = Customer()

    while True:
        if choice == 1:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = [
                "CID",
                "NAME",
                "PHONE",
                "EMAIL",
                "AGE",
                "GENDER",
                "ADDRESS",
                "CREATEDON",
            ]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            pet.cid = customer.cid

            # pet.cid = rows[0][0]

            pet.read_pet_data()
            print(vars(pet))

            sql = pet.get_insert_sql_query()
            db.execute_sql(sql)
            print("Pet Added Successfully...")

        elif choice == 2:
            # Assuming you have the necessary classes and functions defined (customer, pet, db, tabulate, etc.)

            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = [
                "CID",
                "NAME",
                "PHONE",
                "EMAIL",
                "AGE",
                "GENDER",
                "ADDRESS",
                "CREATEDON",
            ]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            if rows:
                customer_fetched = rows[0]
                customer.cid = customer_fetched[0]

                pet.cid = customer.cid
                pet_fetched = rows[0]
                pet.pid = pet_fetched[0]

                pet.name = input("Enter pet's Name: ")
                if len(pet.name) == 0:
                    pet.name = pet_fetched[1]

                pet.age = input("Enter pet's Age: ")
                if len(pet.age) == 0:
                    pet.age = pet_fetched[2]
                else:
                    pet.age = int(pet.age)

                pet.weight = input("Enter pet's weight: ")
                if len(pet.weight) == 0:
                    pet.weight = pet_fetched[3]
                else:
                    pet.weight = int(pet.weight)

                # Update pet's information in the database
                sql = pet.get_update_sql_query()
                db.execute_sql(sql)
                print("Pet Updated...")
            else:
                print("No customer found with the provided phone number.")

        elif choice == 3:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = [
                "CID",
                "NAME",
                "PHONE",
                "EMAIL",
                "AGE",
                "GENDER",
                "ADDRESS",
                "CREATEDON",
            ]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pets_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = [
                "PID",
                "NAME",
                "AGE",
                "WEIGHT",
                "BREED",
                "GENDER",
                "CID",
                "CREATEDON",
            ]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            pet.pid = int(input("Enter Pet Id:"))
            delete_choice = input("Are Your Sure to Delete ? (yes/no): ")

            if delete_choice == "yes":
                sql = pet.get_delete_sql_query()
                db.execute_sql(sql)
                print("Pet Deleted...")

        elif choice == 4:
            sql = pet.get_pets_sql_query()
            rows = db.execute_select_sql(sql)
            columns = [
                "PID",
                "NAME",
                "AGE",
                "WEIGHT",
                "BREED",
                "GENDER",
                "CID",
                "CREATEDON",
            ]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = [
                "CID",
                "NAME",
                "PHONE",
                "EMAIL",
                "AGE",
                "GENDER",
                "ADDRESS",
                "CREATEDON",
            ]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pets_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = [
                "PID",
                "NAME",
                "AGE",
                "WEIGHT",
                "BREED",
                "GENDER",
                "CID",
                "CREATEDON",
            ]
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break
        else:
            print("Invalid Choice")

        print(message)
        choice = int(input("Enter Your Choice: "))
