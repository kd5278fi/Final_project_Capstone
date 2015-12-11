#TODO: create database class, figure out how to save meal plans. Each day is table?

import sqlite3
import datetime
from Classes.FoodItem import *

class Database:

    dbName = "final.db"
    today = datetime.date.today()

    def __init__(self):
        self.conn = sqlite3.connect(self.dbName, timeout=10)
        self.conn.text_factory = str
        self.cursor = self.conn.cursor()

    def setupTables(self):
        self.createTodayTable()

    def createTodayTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ''' + self.today +
                            '''(ndbNO INTEGER PRIMARY KEY,
                            name TEXT,
                            group TEXT,
                            measurement TEXT,
                            time TEXT,
                            calories DECIMAL,
                            carbs DECIMAL,
                            fats DECIMAL,
                            proteins DECIMAL,
                            sugars DECIMAL)''')
        self.conn.commit()

    def dropTodaysTables(self):
        self.cursor.execute('''DROP TABLE IF EXISTS ?''', [self.today])

    def selectAllFromDate(self, day):
        try:
            self.cursor.execute('SELECT * FROM ?', [day])
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
            self.cursor.execute('INSERT INTO ?(ndbNO, name, group, measurement, time, calories, carbs, fats, proteins, sugars) VALUES (?,?,?,?,?,?,?,?,?,?) ', [self.today, food.ndbNO, food.name, food.group, food.measurement, food.time, food.calories, food.carbs, food.fats, food.proteins, food.sugars])
            self.conn.commit()