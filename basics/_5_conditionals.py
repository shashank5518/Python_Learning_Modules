if True:
    print("conditional was true")

if False:
    print("conditional was true")
else:
    print("conditional was false")

language = "Python"

if language == "Python":
    print("conditional was true")
elif language == "Java":
    print("elif was true")
else:
    print("conditional was false")

user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Admin Page")
elif user == "Admin" or logged_in:
    print("Logged in")
else:
    print("Bad Creds")

if not logged_in:
    print("Please log in")
else:
    print("Welcome")

# '==' and 'is'
# None/0/''/[]/{}/() etc are evaluated to false
