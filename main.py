# CNA 350 Realworld Project
# Instructor: Zach Rubin, zrubin@rtc.edu
# Robert Bailey, rmbailey@student.rtc.edu
# Tutor by Thomas Dewey

import mysql.conncetor

def connect():
     # connect address : port
     server_ip = ##the ip address of  your database server##
     con = mysql.connector.connect(host=server_ip, user='maxuser', password='maxpwd', port='4000')
     return con
