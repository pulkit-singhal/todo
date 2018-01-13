#!/usr/bin/env python3
import sqlite3
import sys
import argparse
import textwrap
from itertools import chain, repeat

class ASCIITable(object):
	def __init__(self, headers):
		if type(headers) != list:
			raise TypeError("Header row is expected as a list")
		self.headers = []
		self.data = []
		for i in headers:
			try:
				self.headers.append(str(i))
			except:
				raise ValueError("Unable to convert {} into string".format(i))

	def add_row(self, row):
		if len(self.headers) != len(row):
			raise ValueError("Size of headers and row do not match")
		rowData = []
		for i in row:
			try:
				rowData.append(str(i))
			except:
				raise ValueError("Unable to convert {} into string".format(i))
		self.data.append(rowData)

	def __str__(self):
		columnWidth = []
		asciiTable = ''
		for i in range(len(self.headers)):
			maxWidth = 0
			maxWidth = max(maxWidth, len(str(self.headers[i])))
			for j in range(len(self.data)):
				maxWidth = max(maxWidth, len(str(self.data[j][i]).translate({'\u0336': None})))
			columnWidth.append(maxWidth + 2)
		asciiTable += '+' + '+'.join(map(lambda i: '-' * i, columnWidth)) + '+\n'
		asciiTable += '|' + '|'.join([self.headers[i].center(columnWidth[i]) for i in range(len(columnWidth))]) + "|\n"
		asciiTable += '+' + '+'.join(map(lambda i: '-' * i, columnWidth)) + '+\n'
		for row in self.data:
			asciiTable += '|' + '|'.join([row[i].center(columnWidth[i]) for i in range(len(columnWidth))]) + "|\n"
		asciiTable += '+' + '+'.join(map(lambda i: '-' * i, columnWidth)) + '+'
		return asciiTable

class TodoService(object):
	def __init__(self, filePath):
		self.filePath = filePath
		self.connection = sqlite3.connect(filePath)
		self.connection.cursor().execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)")

	def add_task(self, task):
		self.connection.cursor().execute("INSERT INTO todos (task) VALUES (?)", (task,))

	def remove_tasks(self, id):
		if len(id) != 0:
			self.connection.cursor().execute("DELETE FROM todos WHERE id IN ({})".format(','.join(repeat('?', len(id)))), id)

	def edit_task(self, id, task):
		self.connection.cursor().execute("UPDATE todos SET task = ? WHERE id = ?", (task, id))

	def print_all_tasks(self):
		asciiTable = ASCIITable(["ID", "Task"])
		c = self.connection.cursor()
		c.execute("SELECT * FROM todos")
		for row in c:
			wrapped_task = textwrap.wrap(row[1])
			asciiTable.add_row([row[0], wrapped_task[0]])
			for i in range(1, len(wrapped_task)):
				asciiTable.add_row(['', wrapped_task[i]])
		print(asciiTable)

	def close(self):
		self.connection.commit()
		self.connection.close()

arguments = sys.argv[1:]

filePath = "~/tasks.db"
if arguments[0] == '--location' and len(arguments) >= 2:
	filePath = arguments[1]
	arguments = arguments[2:]

todo = TodoService(filePath)

if len(arguments) == 0:
	todo.print_all_tasks()
elif len(arguments) >= 2 and arguments[0] == "-f":
	todo.remove_tasks(list(map(lambda x: int(x), arguments[1:])))
elif len(arguments) >= 3 and arguments[0] == "-e":
	todo.edit_task(int(arguments[1]), " ".join(arguments[2:]))
else:
	todo.add_task(" ".join(arguments))

todo.close()