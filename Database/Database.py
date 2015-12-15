import sqlite3
import datetime
from Classes.FoodItem import *

class Database:
    #names db for use in connection
    dbName = "final.db"
    #creates string of current date to use as table name. need [] to be accepatable name.
    today = "[" + str(datetime.date.today())+ "]"

    def __init__(self):
        #create connection
        self.conn = sqlite3.connect(self.dbName)
        # self.conn.text_factory = str
        #create cursor which executes code and relates it to database
        self.cursor = self.conn.cursor()

    def setupTables(self):
        self.createTodayTable()
        # self.testInfo()
        # self.testDB()

    def testDB(self):
        self.cursor.execute('''CREATE TABLE TEST
                            (ID INT PRIMARY KEY     NOT NULL,
                            NAME            TEXT    NOT NULL,
                            AGE             INT     NOT NULL,
                            ADDRESS         CHAR(50));''')
        print('Table created')
        self.conn.commit()

    def testInfo(self):
        self.cursor.execute('''INSERT INTO''' + self.today +'''
                            (ndbNO, name, grouptype, measurement, time,
                            calories, carbs, fats, proteins, sugars, quantity)
                            VALUES
                            (1001, 'corn', 'starch', 'cup', 'Dinner',
                            100, 100, 90, 90, 80, 2);''')
        self.conn.commit()

    def createTodayTable(self):
        #checks if today's date is current a table, if not creates new table named with todays string
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS'''+ self.today +'''
                            (foodID     INTEGER PRIMARY KEY AUTOINCREMENT,
                            ndbNO       INT,
                            name        TEXT,
                            grouptype   TEXT,
                            measurement TEXT,
                            time        TEXT,
                            calories    INT,
                            carbs       INT,
                            fats        INT,
                            proteins    INT,
                            sugars      INT,
                            quantity    TEXT);''')
        #commit to database
        self.conn.commit()

    #testing function to drop table
    def dropTodaysTables(self):
        self.cursor.execute('''DROP TABLE IF EXISTS ?''', (self.today))

    #allows a pull of data from table
    def selectAllFromDate(self, day):
        try:
            #pulls all data for date string - use when we can search backlog
            self.cursor.execute('SELECT * FROM [' + str(day) + ']')
            self.conn.commit()
            return self.cursor.fetchall()
        except NameError:
            print("Name Error")
        except ValueError:
            print("Value Error")
        except IOError:
            print("IO Error")

    # save data to today's table
    def save(self, items):
        #save if parameter is more then 0
        if (len(items) != 0):
            for food in items:
                #insert all data by object property
                self.cursor.execute('INSERT INTO ' + self.today + ' (ndbNO, name, grouptype, measurement, time, calories, carbs, fats, proteins, sugars, quantity) VALUES (?,?,?,?,?,?,?,?,?,?,?) ', (food.ndbNO, food.name, food.group, food.measurement, food.time, food.calories, food.carbs, food.fats, food.proteins, food.sugars, food.quantity))
                self.conn.commit()
