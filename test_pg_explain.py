from collections import namedtuple
import time
import psycopg2
import argparse
import csv

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
connection = psycopg2.connect(host = host, database = database, port = port, user = user)
cur = connection.cursor()

with open('tests.sql') as sqlfile:
	with open('sql_output.csv','w') as outfile:
		writer = csv.writer(outfile)
		writer.writerow(['line','plan','time'])
		for line in sqlfile:
			query = 'EXPLAIN ANALYZE '+line.strip()
			cur.execute(query)
			data = cur.fetchall()
			plan = data[0]
			time = data[1]
			writer.writerow([line.strip(),str(plan).strip(),str(time).strip()])
			