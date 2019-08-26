from firebase import firebase

# Get a database reference to our blog.
import firebase_admin
from firebase_admin import credentials

if (not len(firebase_admin._apps)):
    cred = credentials.Certificate('service-account.json')
    default_app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://django-defde.firebaseio.com'})

fbconn = firebase.FirebaseApplication('https://django-defde.firebaseio.com//')

while True:
    name = input("Enter Your Name")
    email = input("Enter Email")
    contact = input("Enter Contact")

    data_to_upload = {
        'Name': name,
        'Email': email,
        'Contact': contact}

    result = fbconn.post('/MyInfo/', data_to_upload)
    print(result)

# To get Data from fireBase

result = fbconn.get('/MyInfo', None)
print(result)