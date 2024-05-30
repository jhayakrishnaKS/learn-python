def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function1(**kid):
  print("His last name is " + kid["lname"])

my_function1(fname = "Tobias", lname = "Refsnes")



def my_function2(country = "Norway"):
  print("I am from " + country)

my_function2("Sweden")
my_function2("India")
my_function2()
my_function2("Brazil")