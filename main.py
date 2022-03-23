## CNE 350 Realworld Project
## Instructor: Zach Rubin, zrubin@rtc.edu
## Robert Bailey, rmbailey@student.rtc.edu
## Tutor by Thomas Dewey

import mysql.connector


def connect():
    # connect address : port
    server_ip = "10.0.0.224"
    con = mysql.connector.connect(host=server_ip, user='maxuser', password='maxpwd', port='4000')
    return con

def question_one(cursor):
    query = "SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 10;"
    cursor.execute(query)
    data = cursor.fetchall()
    print('Last 10 of zipcodes 1')
    for row in data:
        print(row)
    return

def question_two(cursor):
    query = "SELECT Zipcode FROM zipcodes_two.zipcodes_two ORDER BY Zipcode LIMIT 10;"
    cursor.execute(query)
    data = cursor.fetchall()
    print('first 10 of zipcodes 2')
    for row in data:
        print(row)
    return

def question_three(cursor):
    query = "SELECT MAX(DISTINCT Zipcode) FROM zipcodes_one.zipcodes_one;"
    cursor.execute(query)
    data = cursor.fetchall()
    print('Largest in Zipcodes 1')
    print(data)
    return

def question_four(cursor):
    query = "SELECT MIN(DISTINCT Zipcode) FROM zipcodes_two.zipcodes_two;"
    cursor.execute(query)
    data = cursor.fetchall()
    print('Smallest in Zipcodes 2')
    print(data)
    return

def main():
    conn = connect()
    curs = conn.cursor()
    question_one(curs)
    question_two(curs)
    question_three(curs)
    question_four(curs)
    conn.close()

if __name__ == '__main__':
    main()
     
     
     
     
