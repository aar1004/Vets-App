from session14a import DBHelper
from session14 import Customer
from session17 import Consultation
from tabulate import tabulate
from session15 import Pet


def consultation_menu():
    db = DBHelper()

    message = """
    
    >>CONSULATION MENU<<
    0.quit
    1.add consultations
    2.update consultation
    3.view all consultations
    4.view consultations by date
    5.view all customer's pets
    
    """
    print(message)
    choice = int(input("Enter Your Choice:"))

    pet = Pet()
    customer = Customer()
    consultation = Consultation()

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

            if len(rows) == 0:
                print("enter pet first")
                break
            elif len(rows) == 1:
                pet.pid = rows[0][0]
            else:
                print("enter pet id:")

            consultation.cid = customer.cid
            consultation.pid = pet.pid
            consultation.read_consultation_data()

            print(vars(consultation))

            sql = consultation.get_insert_sql_query()
            db.execute_select_sql(sql)
            print("successfully........")

        elif choice == 2:
            pass
        elif choice == 3:
            sql = consultation.get_consultation_sql_query()
            rows = db.execute_select_sql(sql)
            columns = [
                "CNID",
                "CID",
                "PID",
                "PROBLEM",
                "HEARTRATE",
                "TEMPERATURE",
                "MEDICINES",
                "CREATEDON",
            ]
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        elif choice == 4:
            date = input("Enter Date: ")
            sql = consultation.get_consultation_bydate_sql_query(date)
            rows = db.execute_select_sql(sql)
            columns = [
                "CNID",
                "CID",
                "PID",
                "PROBLEM",
                "HEARTRATE",
                "TEMPERATURE",
                "MEDICINES",
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

            pid = int(input("enter pid="))

            sql = consultation.get_consultation_sql_query(pid=str(pet.pid))
            rows = db.execute_select_sql(sql)
            columns = [
                "CNID",
                "CID",
                "PID",
                "PROBLEM",
                "HEARTRATE",
                "TEMPERATURE",
                "MEDICINES",
                "CREATEDON",
            ]

            if len(rows) == 0:
                print("enter pet first")
                break
            elif len(rows) == 1:
                pet.pid = rows[0][0]
            else:
                print("enter pet id:")

            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break
        else:
            print("invalid choice")
        print(message)
        choice = int(input("Enter Your Choice:"))
