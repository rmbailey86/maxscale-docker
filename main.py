# CNA 350 Realworld Project
# Instructor: Zach Rubin, zrubin@rtc.edu
# Robert Bailey, rmbailey@student.rtc.edu
# Tutor by Thomas Dewey

import mysql.conncetor

def connect():
     # connect address : port
     server_ip = 10.0.0.224
     con = mysql.connector.connect(host=server_ip, user='maxuser', password='maxpwd', port='4000')
     return con
def question_one(cursor):
     query = ##SQL query here in quotations##
     cursor.execute(query)
     data = sursor.fetchall()
     print ('Last 10 of zipcodes 1')
     for row in data:
          print (row)
     return   
def question_two(cursor):
     query = ##SQL query here in quotations##
     cursor.execute(query)
     data = sursor.fetchall()
     print ('first 10 of zipcodes 2')
     for row in data:
          print (row)
     return   
