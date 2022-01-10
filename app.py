from flask import Flask
import firebase_admin
import os
from firebase_admin import credentials, firestore, initialize_app

from dotenv import load_dotenv

load_dotenv()


config = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

cred = credentials.Certificate(config)
initialize_app(cred)

db = firestore.client()
products_ref = db.collection('products')

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        products_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
