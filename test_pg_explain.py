from collections import namedtuple
import time
import psycopg2
import argparse

parser = argparse.ArgumentParser(description="Arguments to connect to the db")
parser.add_argument('--verbose','-v',
    action='store_true',
    help='verbose flag' )
parser.add_argument('--port', required=True, help='port flag', type=int)
parser.add_argument('--host', required=True, help='host flag', type=str)
parser.add_argument('--db', required=True, help='database flag', type=str)
parser.add_argument('--user', required=True, help='user flag', type=str)
# parser.add_argument('--password', required=True, help='password flag', type=str)

args = parser.parse_args()


host = args.host
database = args.db
port = args.port
user = args.user
# password = args.password
