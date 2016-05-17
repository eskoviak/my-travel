#!/usr/bin/python
from json import loads
content = open("Expenses.json", "rU").read()
data = loads(content)

print("Expenses:")
print(data["Expense Items"][0]["Date"])
