import mysql.connector as connector
import date
from date import datebro as q
from tabulate import tabulate
class DbObject:
    def __init__(self):
        self.sqluser="your-user"
        self.sqlpass="your-password"
        dateput="Date"+date.dategive()
        CanteenTable = 'create table if not exists canteen(ItemsNo int primary key, ItemsName varchar(32), ItemsPrice int(4), ItemsStock int (4))'
        StudentsTable = 'create table if not exists students(StudentsGR int primary key, studentsName varchar(32), StudentsBalance int(4))'
        Datetable ="create table if not exists {}(PurchaseNo int primary key,StudentsGR int , ItemsNo int, quantity int, time varchar(32), foreign key (ItemsNo) references canteen(ItemsNo) on update cascade on delete cascade, foreign key (StudentsGR) references students(StudentsGR) on update cascade on delete cascade)".format(dateput)
        try:
            self.connection = connector.connect(host = "localhost", user = self.sqluser, passwd = self.sqlpass, database = "SchoolCanteen")
            MakeCursor = self.connection.cursor()
            print("Database exists and using it")
        except:
            self.connection= connector.connect(host = "localhost", user = self.sqluser, passwd = self.sqlpass)
            if self.connection.is_connected():
                print("Successfully Connected")
            else:
                exit()
            MakeCursor = self.connection.cursor()
            MakeCursor.execute("create database SchoolCanteen;")
            print("Successfully Created database")
        MakeCursor.execute(Datetable)
        MakeCursor.execute(CanteenTable)
        MakeCursor.execute(StudentsTable)
    def CheckPass(self):
        return(self.sqlpass)
    def CheckUser(self):
        return(self.sqluser)
    #To insert data in the table of Canteen
    def AddCanteenData(self, Id, Name, Price, Stock):  #these are new variable
        query = "insert into canteen(ItemsNo, ItemsName, ItemsPrice, ItemsStock) values({},'{}',{},{})". format(Id, Name, Price, Stock)
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        print('Data saved /n ----------------')
    #To insert data in the table of Canteen
    def AddStudentData(self, Id, Name, Balance):  #these are new variable
        query = "insert into students(StudentsGR, studentsName, StudentsBalance) values({},'{}',{})". format(Id, Name, Balance)
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        print('Data saved')
    #To Fetch all data from the table of database
    def FetchCanteen(self):
        query = "select * from canteen"
        cur = self.connection.cursor()
        cur.execute(query)
        listcanteen = []
        for i in cur:
              listcanteen.append(i)
              
        return(listcanteen)
    def LenghtCanteenItem(self):
        query = "select * from canteen"
        cur = self.connection.cursor()
        cur.execute(query)
        getList= []
        for i in cur:
            getList.append(i[0])

        lenght = len(getList)
        return(lenght)
    #To Fetch all data from the table of students
    def FetchStudent(self):
        query = "select * from students"
        cur = self.connection.cursor()
        cur.execute(query)
        listStudent = []
        for i in cur:
              listStudent.append(i)
        return(listStudent)
    def FetchLastId(self):
        dateput="Date"+date.dategive()
        query="SELECT PurchaseNo FROM {} WHERE PurchaseNo=(SELECT max(PurchaseNo) FROM {});".format(dateput,dateput)
        cur = self.connection.cursor()
        cur.execute(query)
        d=cur.fetchall()
        print(d)
        if d==[]:
            d=0
            return(d)
        else:
            return(d[0][0])
    def Fetchdate(self):
        dateput="Date"+date.dategive()
        query = "select * from {}".format(dateput)
        cur = self.connection.cursor()
        cur.execute(query)
        listdate = []
        for i in cur:
              listdate.append(i)
              
        return(listdate)
    # To eftch GR Number from the table of student
    def GR(self):
        query = "select * from students"
        cur = self.connection.cursor()
        cur.execute(query)

        GrList= []
        for i in cur:
            GrList.append(i[0])

        return(GrList)

    # To update a data from the table of canteen
    def UpdatCanteen(self, Id, nName, nPrice, nStock): # nName New name as variable
        quer = "update canteen set ItemsName='{}', ItemsPrice={}, ItemsStock={} where ItemsNo={}".format(nName, nPrice, nStock, Id)

        cur = self.connection.cursor()
        cur.execute(quer)
        self.connection.commit()
        print("Data Updated") 

    # To update a data from the table of students
    def UpdatStudent(self, Id, nName, nBalance): # nName New name as variable
        quer = "update students set studentsName='{}', StudentsBalance={} where StudentsGR={}".format(nName, nBalance, Id)
        cur = self.connection.cursor()
        cur.execute(quer)
        self.connection.commit()
        print("Data Updated") 

        
    def dropdate(self):
        dateput="Date"+str(int(date.dategive())-1)
        print(dateput)
        quer ="drop table {}".format(dateput)
        print(quer)
        cur = self.connection.cursor()
        cur.execute(quer)
        self.connection.commit()
        print("Data Updated") 

        
    def adddate(self, ch, Id, ItemNo, quantity, time):
        dateput="Date"+date.dategive()
        quer="insert into {} values({},{},{},{},'{}')". format(dateput, ch, Id, ItemNo, quantity, time)
        cur = self.connection.cursor()
        cur.execute(quer)
        self.connection.commit()
        print("Data Updated")

    def display(self, a):
        if a==1:
            query="select * from canteen;"
            cur = self.connection.cursor()
            cur.execute(query)
            d=cur.fetchall()
            print(tabulate(d,headers=['ItemsNo','ItemsName','ItemsPrice','ItemsStock'],tablefmt='psql'))

        elif a==2:
            query="select * from students;"
            cur = self.connection.cursor()
            cur.execute(query)
            d=cur.fetchall()
            print(tabulate(d,headers=['StudentsGR', 'studentsName','StudentsBalance'],tablefmt='psql'))
        else:
            print("Invalid Input")
    def canteenidsearch(self, Id):
        try:
            b=int(Id)
            query="select * from canteen where ItemsNo={};".format(b)
        except:
            b=str(Id)
            query='select * from canteen where ItemsName like "%{}%";'.format(b)
        try:
            print(query)
            cur = self.connection.cursor()
            cur.execute(query)
            d=cur.fetchall()
            print(query)
            return(d)
        except:
            print("Error")

    def studentidsearch(self, Id):
        try:
            b=int(Id)
            query="select * from students where StudentsGr={};".format(b)
        except:
            b=str(Id)
            query='select * from students where StudentsName like "%{}%";'.format(b)
        try:
            print(query)
            cur = self.connection.cursor()
            cur.execute(query)
            d=cur.fetchall()
            print(query)
            return(d)
        except:
            print("Error")
    def studentbalancesearch(self, Id):
        try:
            b=int(Id)
            query="select studentsbalance from students where StudentsGr={};".format(b)
        except:
            b=str(Id)
            query='select studentsbalance from students where StudentsName like "%{}%";'.format(b)
        try:
            print(query)
            cur = self.connection.cursor()
            cur.execute(query)
            d=cur.fetchall()
            print(query)
            return(d[0][0])
        except:
            print("Error")
    def UpdatStudentbalance(self, Id, nBalance): # nName New name as variable
        quer = "update students set StudentsBalance={} where StudentsGR={}".format(nBalance, Id)
        cur = self.connection.cursor()
        cur.execute(quer)
        self.connection.commit()
        print("Data Updated")
    def dropcanteen(self, Id):
        query="delete from canteen where ItemsNo={}".format(Id)
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        print("Data Updated")
    def dropstudent(self, Id):
        query="delete from students where StudentsGr={}".format(Id)
        cur = self.connection.cursor()
        cur.execute(query)
        self.connection.commit()
        print("Data Updated")
SchoolDatabase = DbObject()
