import pyrebase

config = {
  "apiKey": "$APIKEYHERE",
  "authDomain": "django-test-271501.firebaseapp.com",
  "databaseURL": "https://django-test-271501.firebaseio.com",
  "storageBucket": "django-test-271501.appspot.com",
  "serviceAccount": "/Users/kwilson/django-test-271501-firebase-adminsdk-u89uu-07803e6c75.json"
}


firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Get a reference to the database service
db = firebase.database()