from types import NoneType
import psycopg2
import time
from dotenv import load_dotenv
import os

def connect():
    
    load_dotenv()

    connection = psycopg2.connect(
        host=os.environ.get('host'),
        database=os.environ.get('database'),
        user=os.environ.get('username'),
        password=os.environ.get('password'),
        sslmode='require'
    )

    return connection

