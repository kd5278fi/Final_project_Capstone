import sqlite3
import datetime
from Classes.FoodItem import *

class Database:

    dbName = "final.db"
    today = "[" + str(datetime.date.today())+ "]"

    def __init__(self):
        self.conn = sqlite3.connect(self.dbName)
        # self.conn.text_factory = str
        self.cursor = self.conn.cursor()

    def setupTables(self):
        self.createTodayTable()
        self.testInfo()
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
                            (1001, 'corn', 'starch', 'cup', 'dinner',
                            100, 100, 90, 90, 80, 2);''')
        self.conn.commit()

    def createTodayTable(self):
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
        self.conn.commit()

    def dropTodaysTables(self):
        self.cursor.execute('''DROP TABLE IF EXISTS ?''', (self.today))

    def selectAllFromDate(self, day):
        try:
            self.cursor.execute('SELECT * FROM [' + str(day) + ']')
            self.conn.commit()
            return self.cursor.fetchall()
        except NameError:
            print("Name Error")
        except ValueError:
            print("Value Error")
        except IOError:
            print("IO Error")

    def save(self, items):
        for food in items:
            self.cursor.execute('INSERT INTO ?(ndbNO, name, grouptype, measurement, time, calories, carbs, fats, proteins, sugars, quantity) VALUES (?,?,?,?,?,?,?,?,?,?,?) ', (self.today, food.ndbNO, food.name, food.group, food.measurement, food.time, food.calories, food.carbs, food.fats, food.proteins, food.sugars, food.quantity))
            self.conn.commit()