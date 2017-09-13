#!usr/bin/env python3

import MySQLdb

# Adding Signup details to investors account
def add_inv(username,email,password):
	connection = MySQLdb.connect(host="localhost",
								user="root",
								passwd="Aki2907d",
								db="invent")
	cursor = connection.cursor()
	cursor.execute(
		'''INSERT INTO investors(
			username,
			email,
			password
		)VALUES(%s,%s,%s);''',
		(username,email,password)
	)
	connection.commit()
	connection.close()

# Signing In to investors account
class InvLogin:
	def __init__(self, objectified_username, objectified_password):
		self.objectified_username = objectified_username
		self.objectified_password = objectified_password

	def lookup_username(uname):
		connection = MySQLdb.connect(host="localhost",
									user="root",
									passwd="Aki2907d",
									db="invent")
		cursor = connection.cursor()
		objectified_username = cursor.execute(
		'''SELECT username FROM investors WHERE username="{}";'''.format(uname))
		data = cursor.fetchall()

		connection.commit()
		connection.close()
		return data[0][0]

	def lookup_password(uname):
		connection = MySQLdb.connect(host="localhost",
									user="root",
									passwd="Aki2907d",
									db="invent")
		cursor = connection.cursor()
		objectified_password = cursor.execute(
		'''SELECT password FROM investors WHERE username="{}";'''.format(uname))        
		data = cursor.fetchall()

		connection.commit()
		connection.close()
		return data[0][0]

# Adding other details to investors account
def insert_inv_details(uname, firstname, lastname, comp_name):
    connection = MySQLdb.connect(host="localhost",
								user="root",
								passwd="Aki2907d",
								db="invent")
    cursor = connection.cursor()

    cursor.execute('''UPDATE investors SET firstname="{}", lastname="{}", comp_name="{}"
        WHERE username = "{}";'''.format(firstname,lastname,comp_name,uname))

    connection.commit()
    connection.close()

#Accessing Pitch Messages from all the Entrepreneurs
def get_pitch_msg():
	connection = MySQLdb.connect(host="localhost",
								user="root",
								passwd="Aki2907d",
								db="invent")
	cursor = connection.cursor()

	cursor.execute('''SELECT username, pitch_msg FROM entrepreneurs;''')
	data = cursor.fetchall()

	connection.commit()
	connection.close()
	return data


# Adding Signup details to entrepreneurs account
def add_ent(username,email,password):
	connection = MySQLdb.connect(host="localhost",
								user="root",
								passwd="Aki2907d",
								db="invent")
	cursor = connection.cursor()
	cursor.execute(
		'''INSERT INTO entrepreneurs(
			username,
			email,
			password
		)VALUES(%s,%s,%s);''',
		(username,email,password)
	)
	connection.commit()
	connection.close()

# Signing In to entrepreneurs account
class EntLogin:
	def __init__(self, objectified_username, objectified_password):
		self.objectified_username = objectified_username
		self.objectified_password = objectified_password

	def lookup_username(uname):
		connection = MySQLdb.connect(host="localhost",
									user="root",
									passwd="Aki2907d",
									db="invent")
		cursor = connection.cursor()
		objectified_username = cursor.execute(
		'''SELECT username FROM entrepreneurs WHERE username="{}";'''.format(uname))
		data = cursor.fetchall()

		connection.commit()
		connection.close()
		return data[0][0]

	def lookup_password(uname):
		connection = MySQLdb.connect(host="localhost",
									user="root",
									passwd="Aki2907d",
									db="invent")
		cursor = connection.cursor()
		objectified_password = cursor.execute(
		'''SELECT password FROM entrepreneurs WHERE username="{}";'''.format(uname))        
		data = cursor.fetchall()

		connection.commit()
		connection.close()
		return data[0][0]

# Adding other details to entrepreneurs account
def insert_ent_details(uname, firstname, lastname, heading, project_desc, web_link, pitch_msg):
    connection = MySQLdb.connect(host="localhost",
								user="root",
								passwd="Aki2907d",
								db="invent")
    cursor = connection.cursor()

    cursor.execute('''UPDATE entrepreneurs SET firstname="{}", lastname="{}", heading="{}", project_desc="{}", web_link="{}", pitch_msg="{}"
        WHERE username = "{}";'''.format(firstname,lastname,heading,project_desc,web_link,pitch_msg,uname))

    connection.commit()
    connection.close()