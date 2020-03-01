# DIT.py
# Modifying data stored in collections
# Creating methods, functions or procedures that use parameters & / or return values.

#you can use more than one parameter in a function but seperate them with a comma.
def function_names(name, lname):
    print(name + " " + lname)
#you have to clasify both functions to avoid an error.
function_names("Lee", "Child")
function_names("Stephen", "King")
function_names("Jane", "Austin")

def function_workstation(*workstation):
    print("Lee is manning the " + workstation[2])

function_workstation("cashier", "sink", "kitchen", "tables")

#a list as an argument
def function_pizza(pizzas):
    for x in pizzas:
        print(x)
#list
pizzas = ["Hawaiin", "Peperoni", "Greek", "Vegetarian", "BBQ Chicken", "Meat Lovers"]
function_pizza(pizzas) 

#return values
def function_prices(a):
   return 5 * a
#useing these to multiply the price by the amount of pizzas baught  
print(function_prices(1))
print(function_prices(2))
print(function_prices(3))
print(function_prices(4)) 

#starts at 1 then adds the next number, i.e. 1 + 2, 3 + 3, 6 + 4, 10 + 5, 15 + 6. 
#this stops as soon as it reaches the value set as (k)

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)

    else:
        result = 0
    return result

tri_recursion(9) 
#putting (x) gives the int of the amount of numbers / the numbers that should be used
