import os
from flask import request
from flask import render_template
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, String
from models import *
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgres://qrekofxwyhgwcj:82fd5fb1229b5654ad1dd2b62b1ce0a1a17a75ccfb14383fcde72596b4ba6096@ec2-18-210-51-239.compute-1.amazonaws.com:5432/dccfi7g45ons6d"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    print("Creating tables")
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()