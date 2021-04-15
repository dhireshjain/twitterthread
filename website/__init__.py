from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

from website.views import general

app.register_blueprint(general.mod)
