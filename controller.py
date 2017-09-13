#!usr/bin/env python3

import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mysqldb import MySQL
from wtforms import Form, TextField, StringField, TextAreaField, BooleanField, PasswordField, fields, validators
import model

# MySQL Configurations
mysql = MySQL()
app = Flask(__name__)
app.config['SECRET_KEY'] = '9876543210'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Aki2907d'
app.config['MYSQL_DATABASE_DB'] = 'invent'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
username_inv="mike"
username_ent="bill"
pitch_msg="test"

# Router for Homepage
@app.route('/')
def show_homepage():
	return render_template('index.html')

# Class for Signup and Signin
class Register(Form):
    username = StringField('Username : ', [validators.DataRequired()])
    email = TextField('Email : ', [validators.DataRequired()])
    password = PasswordField('Password : ', [validators.DataRequired()])

# Handling Investor's Signup
@app.route('/inv_signup', methods=['GET', 'POST'])
def inv_signup():
    form = Register(request.form)
    if request.method == 'POST':
        if form.validate() == True:
            global username_inv
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            model.add_inv(username,email,password)
            return redirect(url_for('inv_signin'))
        else:
            return render_template('inv_signup.html', form=form)
    elif request.method == 'GET':
        return render_template('inv_signup.html', form=form)

# Handling Investor's Signin
@app.route('/inv_signin', methods=['GET', 'POST'])
def inv_signin():
    error = None
    if request.method == 'POST':
        global username_inv
        username_inv = request.form.get('username')
        submitted_username   = request.form.get('username')
        submitted_password   = request.form.get('password')
        objectified_username = model.InvLogin.lookup_username(submitted_username)
        objectified_password = model.InvLogin.lookup_password(submitted_username)
        model.InvLogin(objectified_username, objectified_password)
        if request.form['username'] != objectified_username or request.form['password'] != objectified_password:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('inv_account'))
    return render_template('inv_signin.html', error=error)

# Handling Entrepreneurs's Signup
@app.route('/ent_signup', methods=['GET', 'POST'])
def ent_signup():
    form = Register(request.form)
    if request.method == 'POST':
        if form.validate() == True:
            global username_ent
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            model.add_ent(username,email,password)
            return redirect(url_for('ent_signin'))
        else:
            return render_template('ent_signup.html', form=form)
    elif request.method == 'GET':
        return render_template('ent_signup.html', form=form)

# Handling Entrepreneurs's Signin
@app.route('/ent_signin', methods=['GET', 'POST'])
def ent_signin():
    error = None
    if request.method == 'POST':
        global username_ent
        username_ent = request.form.get('username')
        submitted_username   = request.form.get('username')
        submitted_password   = request.form.get('password')
        objectified_username = model.EntLogin.lookup_username(submitted_username)
        objectified_password = model.EntLogin.lookup_password(submitted_username)
        model.EntLogin(objectified_username, objectified_password)
        if request.form['username'] != objectified_username or request.form['password'] != objectified_password:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('ent_account'))
    return render_template('ent_signin.html', error=error)

# Class for Investor's details
class InvAccount(Form):
    firstname = StringField('First Name : ', [validators.DataRequired()])
    lastname = StringField('Last Name : ', [validators.DataRequired()])
    comp_name = StringField('Company Name : ', [validators.DataRequired()])

# Entering Investor's Details
@app.route('/inv_account', methods=['GET', 'POST'])
def inv_account():
    global username_inv
    form = InvAccount(request.form)
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        comp_name = request.form['comp_name']
        model.insert_inv_details(username_inv, firstname, lastname, comp_name)
        data = model.get_pitch_msg()
        ent_uname = []
        ent_pitch = []
        for i in range(0, len(data)):
            ent_pitch.append(data[i][1])
            ent_uname.append(data[i][0])
        return render_template('inv_user.html', ent_uname=ent_uname, ent_pitch=ent_pitch, firstname=firstname, lastname=lastname, comp_name=comp_name)
    elif request.method == 'GET':
        return render_template('inv_account.html', form=form)

# Class for Entrepreneur's details
class EntAccount(Form):
    firstname = StringField('First Name : ', [validators.DataRequired()])
    lastname = StringField('Last Name : ', [validators.DataRequired()])
    heading = TextField('Heading : ', [validators.DataRequired()])
    project_desc = TextAreaField('Project Description : ', [validators.DataRequired()])
    web_link = TextField('Website Address : ', [validators.DataRequired()])
    pitch_msg = TextAreaField('Pitch Message : ', [validators.DataRequired()])

# Entering Entrepreneur's Details
@app.route('/ent_account', methods=['GET', 'POST'])
def ent_account():
    global username_ent
    form = EntAccount(request.form)
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        heading = request.form['heading']
        project_desc = request.form['project_desc']
        web_link = request.form['web_link']
        pitch_msg = request.form['pitch_msg']
        model.insert_ent_details(username_ent, firstname, lastname, heading, project_desc, web_link, pitch_msg)
        return render_template('ent_user.html', firstname=firstname, lastname=lastname, heading=heading, project_desc=project_desc, web_link=web_link, pitch_msg=pitch_msg)
    elif request.method == 'GET':
        return render_template('ent_account.html', form=form)

# Handling Investor User's page
@app.route('/inv_user')
def inv_user():
	return render_template('inv_user.html')

# Handling Entrepreneur User's page
@app.route('/ent_user')
def ent_user():
	return render_template('ent_user.html')

# Router for About page
@app.route('/about')
def about_us():
    return render_template('about.html')

# Router for Investors page
@app.route('/investors')
def investors():
    return render_template('investors.html')

# Router for Entrepreneurs page
@app.route('/entrepreneurs')
def entrepreneurs():
    return render_template('entrepreneurs.html')

# Router for FAQ page
@app.route('/faq')
def faq_page():
	return render_template('faq.html')

# Router for Contact page
@app.route('/contact')
def contact_us():
	return render_template('contact.html')

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)
