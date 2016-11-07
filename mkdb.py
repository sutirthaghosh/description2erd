import sqlite3
import csv


def createdb(dbname):
    global conn
    conn = sqlite3.connect(dbname)


def createtable(tablename,filename):
    query = "CREATE TABLE IF NOT EXISTS "+tablename+"(id INTEGER,name text)"
    print(query)
    conn.execute(query)
    with open("csvdata/"+filename, encoding= 'utf-8') as dbfile:
        for row in csv.reader(dbfile):
            print(row)
            tup = (row[0], row[1])
            query = "INSERT INTO "+tablename+" VALUES (?,?)"
            conn.execute(query, tup)
    conn.commit()


def printtable(tablename):
    """prints the table identified by tablename"""
    query = "SELECT * FROM "+tablename
    for row in conn.execute(query):
        print(row)


def searchname(name,stname,btname):
    """if found returns basename else return false,stname is synonymtable name and bname is basetablename"""
    query1 = "SELECT * FROM "+stname+" WHERE name=?"
    tup1 = (name,)
    cur = conn.cursor()
    row = cur.execute(query1, tup1)
    row = row.fetchone()
    if row is not None:
        print(row[1])
    else:
        return print('not found')
    query2 = "SELECT * FROM "+btname+" WHERE id=?"
    tup2= (row[0],)
    row = cur.execute(query2, tup2)
    row = row.fetchone()
    if row is not None:
        print(row[1])
        return row[1]


if __name__ == '__main__':
    createdb('words.db')
    #createtable('Ename_base', 'Ename_base.csv')
    #createtable('Ename_synonym', 'Ename_synonym.csv')
    printtable('Ename_base')
    printtable('Ename_synonym')
    searchname('boy', 'Ename_synonym', 'Ename_base')
    conn.close()


