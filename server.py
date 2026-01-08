from firebase_admin import credentials, initialize_app, firestore
import firebase_admin
import os

credentials = credentials.Certificate('database.json')
firebase_admin.initialize_app(credentials)
database =firestore.client()

def new(username, name, email, password):
    database.collection('stax_users').add({
        'username' : username,
        'name' : name,
        'email' : email,
        'password' : password
    
    })


def is_new_email(email):
    user_ref = database.collection('stax_users').where('email', '==', email).get()
    return len(user_ref) == 0 

def is_new_username(username):
    user_ref = database.collection('stax_users').where('username', '==', username).get()
    return len(user_ref) == 0

def get_email_by_username(username):
    user_ref = database.collection("stox_users").where('username', '==', username).get()
    if len(user_ref) > 0:
        return user_ref[0].to_dict()['email']
    return False                                           #False if username foes not exists

def get_password_by_username(username):
    user_ref = database.collection("stox_users").where('username', '==', username).get()
    if len(user_ref) > 0:
        return user_ref[0].to_dict()['password']
    return False                                           #False if username foes not exists

def username_by_email(email):
    user_ref = database.collection("stox_users").where('email', '==', email).get()
    if len(user_ref) > 0:
        return user_ref[0].to_dict()['username']
    return False                                           #False if username foes not exists

def get_name_by_username(username):
    user_ref = database.collection("stox_users").where('username', '==', username).get()
    if len(user_ref) > 0:
        return user_ref[0].to_dict()['name']
    return False                                           #False if username foes not exists

def correct_credentials(username, password):
    if is_new_username(username):
        return False
    if get_password_by_username(username) == password:
        return True
    return False

