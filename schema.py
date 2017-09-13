#!usr/bin/env python3

import MySQLdb

connection = MySQLdb.connect(host="localhost",
							user="root",
							passwd="Aki2907d",
							db="invent")
cursor = connection.cursor()


cursor.execute(
	'''CREATE TABLE IF NOT EXISTS investors(
		inv_id BIGINT AUTO_INCREMENT,
		username VARCHAR(64),
		email VARCHAR(128),
		password VARCHAR(64),
		firstname VARCHAR(128),
		lastname VARCHAR(128),
		comp_name VARCHAR(256),
		PRIMARY KEY (inv_id)
	);'''
)

cursor.execute(
	'''INSERT INTO investors(
		username,
		email,
		password,
		firstname,
		lastname,
		comp_name
		) VALUES(
		"nmodi",
		"nar_modi@indiangov.in",
		"india123",
		"Narendra",
		"Modi",
		"Hello Corporation Ltd."
		);'''
)

cursor.execute(
	'''CREATE TABLE IF NOT EXISTS entrepreneurs(
		ent_id BIGINT AUTO_INCREMENT,
		username VARCHAR(64),
		email VARCHAR(128),
		password VARCHAR(64),
		firstname VARCHAR(128),
		lastname VARCHAR(128),
		heading VARCHAR(256),
		project_desc VARCHAR(2048),
		web_link VARCHAR(256),
		pitch_msg VARCHAR(140),
		PRIMARY KEY (ent_id)
	);'''
)

cursor.execute(
	'''INSERT INTO entrepreneurs(
		username,
		email,
		password,
		firstname,
		lastname,
		heading,
		project_desc,
		web_link,
		pitch_msg
		) VALUES(
		"ajaitly",
		"arun_j@indiangov.in",
		"india987",
		"Arun",
		"Jaitly",
		"My Business Idea",
		"This is the description of my business idea",
		"www.myproject.com",
		"This is my Pitch Message for the Investors"
		);'''
)


connection.commit()
cursor.close()
connection.close()