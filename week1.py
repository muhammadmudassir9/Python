'''
def myfun(fname, lname):
    print(fname, lname)


myfun("muhammad")

def myfun(*kids):
    print("The youngest child is", kids[0])

myfun("md","ali","mz")

def myfun(child1, child2, child3):
    print("The youngest child is", child3)

myfun(child1 ="md", child2 ="ali", child3= "mz")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Mudassar")


def myfun(cars):
    for i in cars:
        print(i)
cars= ["Toyota","Honda","BMW","Mercedes"]

myfun(cars)



def my_function(x, /):
  print(x)

my_function(3)
'''

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)