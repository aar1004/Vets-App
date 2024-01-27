# create table Customer(
#     cid int primary key auto_increment,
#     name text,
#     phone text,
#     email text
# );

# describe Customer

# insert into Customer values(null,'john','567890987654','john@example.com')

import mysql.connector as db


class Customer:
    def __init__(self):
        self.name = input("enter customer name:")
        self.phone = input("enter phone number:")
        self.email = input("enter email:")


def main():
    customer = Customer()
    print(vars(customer))

    # database connectivity

    # step 1:create connection with database
    connection = db.connect(
        user="root", password="root", host="127.0.0.1", database="datads"
    )

    # obtain cursor to perform operations
    cursor = connection.cursor()

    # create sql statements
    sql = "insert into Customer values(null,'{name}','{phone}','{email}');".format_map(
        vars(customer)
    )

    # execute sql command
    cursor.execute(sql)
    connection.commit()

    print("customer inserted...")


if __name__ == "__main__":
    main()
