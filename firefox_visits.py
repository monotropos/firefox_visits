#!/usr/bin/python3
import sys
import sqlite3
from sqlite3 import Error
from datetime import datetime
# from dateutil import parser


def open_db(dfile):
	"""create a database connection to the SQLite database specified by the dfile
	:dfile: which SQLite file to open
	:returns: db connection
	"""
	conn = None
	try:
		conn = sqlite3.connect(dfile)
	except Error as e:
		print(e)
	return conn


def main(argv):
	if len(argv) == 1:
		print("Usage: " + argv[0] + " <places.sqlite>")
		sys.exit(1)

	conn = open_db(argv[1])
	if conn is None:
		sys.exit(2)

	when = datetime.now().timestamp()
	cur = conn.cursor()
	sql = "SELECT title, url, visit_count FROM moz_places WHERE last_visit_date > " + when
	cur.execute(sql)
	rows = cur.fetchall()

	for row in rows:
		print(row)


if __name__ == '__main__':
	main(sys.argv)
