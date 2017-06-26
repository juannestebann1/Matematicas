# coding=utf-8
import MySQLdb
import sqlite3
import os
import configure as cf

DB_HOST = cf.DB["HOST"] 
DB_USER = cf.DB["USER"] 
DB_PASS = cf.DB["PASSWORD"]
DB_NAME = cf.DB["DATABASE"]
DB_MODE = cf.DB["MODE"]

def connection_Online():
    DATA = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
    return MySQLdb.connect(*DATA)

def connection_Offline():
    DATA = DB_NAME + ".db"
    if os.path.isfile(DATA):
    	return sqlite3.connect(DATA)
    else:
        raise

def connection():
 	if DB_MODE:
 		return connection_Online()
 	else:
 		return connection_Offline()

def WHERE_SET(where="", st=False):
    wheres = ""
    if where != "":
        where_cont = len(where)
        contA = 0
        contB = 1

        if st == "1":
            wheresM = " SET "
        else:
            wheresM = " WHERE "

        while (contB < where_cont):
            wheres = wheres + where[contA] + " = '" + where[contB]

            if contB+1 == where_cont:
                wheres = wheres + "'"
            else:
            	if st == "1":
                	wheres = wheres + "', "
                else:
                	wheres = wheres + "' AND "

            contA = contA + 2
            contB = contB + 2

        wheres = wheresM + wheres
        return wheres
    else:
        return wheres

def INTO(value):
    if value != "":
        value_cont = len(value)
        contA = 0
        contB = 1
        values = ""
        c = ""
        v = ""

        while (contB < value_cont):
            c = c + str(value[contA])
            v = v + "'" + str(value[contB])
            if contB+1 == value_cont+1/2:
                c = c + ")"
                v = v + "')"
            else:
                c = c + ", "
                v = v + "', "

            contA = contA+2
            contB = contB+2

        values = " (" + c + " VALUES (" + v + ''
        return values
    else:
        return values

def SELECT(column="*", table="", where=""):
    conn = connection()
    cursor = conn.cursor()
    wheres = " "
    wheres = WHERE_SET(where)
    query = "SELECT "+ column +" FROM "+ table + wheres
    cursor.execute(query)
    if wheres != "":
        result = cursor.fetchall()
        if len(result) > 0:
            return result[0]
        else:
            return None
    else:
        return cursor.fetchall()
    
def INSERT(table="", values=""):
	conn = connection()
	cursor = conn.cursor()
	insert = " "
	inserts = INTO(values)
	query = "INSERT INTO " + table + inserts + " "
	cursor.execute(query)
	conn.commit()

def UPDATE(table="", setsv="", where="", all="false"):
	conn = connection()
	cursor = conn.cursor()
	sets = " "
	wheres = " "
	sets = WHERE_SET(setsv, "1")
	wheres = WHERE_SET(where)
	query = "UPDATE "+ table + sets + wheres
	cursor.execute(query)
	conn.commit()

def DELETE(table="", where="", all="false"):
	conn = connection()
	cursor = conn.cursor()
	wheres = " "
	wheres = WHERE_SET(where)
	query = "DELETE FROM "+ table + wheres
	cursor.execute(query)
	conn.commit()