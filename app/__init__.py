from flask import Flask

app = Flask(__name__)
app.secret_key = "v5mqvgwj"

from app import views