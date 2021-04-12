#!/usr/bin/python3
import sys
import datetime
# from dateutil import parser
import sqlite3
from sqlite3 import Error


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

	when = datetime.datetime.now() - datetime.timedelta(days=1)
	when = int(when.timestamp() * 1000000)
	cur = conn.cursor()
	sql = "SELECT title, url, visit_count FROM moz_places WHERE last_visit_date > " + str(when) + " ORDER BY last_visit_date"
	cur.execute(sql)
	rows = cur.fetchall()

	for row in rows:
		if row[0] is None:
			title = "–"
		else:
			title = row[0]
		try:
			print(title + "\t" + row[1] + "\t(" + str(row[2]) + ")")
		except TypeError:
			print(row)


if __name__ == '__main__':
	main(sys.argv)
