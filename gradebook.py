gradebook = {
    "Alice": "A",
    "Bryan": "B",
    "Charlie": "A-"
}

name = input("What is the studnet's name? ")
print(gradebook.get(name))

if gradebook.get(name):
    print("Found it")
else:
    print("Student not found.")