import firebase_admin
from firebase_admin import credentials

from flask import Flask

cred = credentials.Certificate(r"C:\Users\anikate koul\OneDrive\Desktop\Chat-App-Backend\firebaseCredentials.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


app.run(debug=True)

