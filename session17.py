# create table Consultation(
#         cnid int primary key auto_increment,
#         cid int;
#         pid int;
#         problem text,
#         heartrate int,
#         temperature float,
#         medicines text,
#         createdon datetime,
#         FOREIGN KEY (cid) REFERENCES Customer(cid),
#         FOREIGN KEY (pid) REFERENCES Pet(pid)
#     );


import datetime


class Consultation:
    def __init__(self):
        self.cnid = 0
        self.cid = 0
        self.pid = 0
        self.problem = ""
        self.heartrate = 0
        self.temperature = 98.6
        self.medicines = 0
        self.createdon = ""

    def read_consultation_data(self):
        self.problem = input("enter problem:")
        self.heartrate = int(input("enter heartrate:"))
        self.temperature = input("enter temperature:")
        self.medicines = input("enter medicine:")

        self.createdon = str(datetime.datetime.today())
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = (
            "insert into Consultation values(null,{cid},{pid}, '{problem}', {heartrate}, {temperature},"
            "'{medicines}','{createdon}');".format_map(vars(self))
        )
        return sql

    def get_consultation_sql_query(self, cid="", pid=""):
        if len(pid) != 0:
            sql = "select * from Consultation where pid = {}".format(pid)
        elif len(cid) != 0:
            sql = "select * from Consultation where cid = {}".format(cid)
        else:
            sql = "select * from Consultation"

        return sql

    def get_consultation_bydate_sql_query(self, date=""):
        sql = "select * from Consultation where createdon = {}".format(date)
        return sql

    def get_delete_sql_query(self):
        sql = "delete from Consultation where cnid = {};".format(self.cnid)
        return sql

    def get_update_sql_query(self):
        sql = "update Pet set name='{name}', age={age}, weight={weight},breed='{}',gender='{}',cid='{cid}',createdon='{createdon}' where pid = {pid};".format_map(
            vars(self)
        )
        return sql
