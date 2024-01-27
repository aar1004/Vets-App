import mysql.connector as db


class DBHelper:
    def __init__(self):
        self.connection = db.connect(
            user="root", password="root", host="127.0.0.1", database="datads"
        )

        self.cursor = self.connection.cursor()

        print("[DBHelper] connection created and cursor obtained")

    # Insert, Update and Delete i.e. Write into Database
    def execute_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        # Step3: Execute SQL Command
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] SQL Statement Executed...")

    # Select Operation i.e. Read from Database
    def execute_select_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        # Step3: Execute SQL Command
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
