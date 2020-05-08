# DIT.py
# Modifying data stored in collections
# Creating methods, functions or procedures that use parameters & / or return values.

def function_name(name, lname):
	print(name + " " + lname)
	
function_name("Lee", "Child")
function_name("Stephen", "King")
function_name("Terry", "Pratchet")

def function_workstation(*workstation)
	print("Lee is manning the " + workstation[2])

function_workstation("kitchen", "sink", "cashier", tables")

def function_pizza(pizzas):
	for x in pizzas:
		print(x)

pizzas = ["Hawaiin", "Peperoni", "Vegetarian", "Greek", "BBQ Chicken"]

function_pizza(pizzas)

def function_prices(a):
	return 5 * a

print(function_pizza(1))
print(function_pizza(2))
print(function_pizza(3))
print(function_pizza(4))
print(function_pizza(5))

def tri_recursion(k):
	if (k > 0):
		result = k + tri_recursion (k -1)
		
	else:
		result = 0
	return result
	
tri_recursion(9)
