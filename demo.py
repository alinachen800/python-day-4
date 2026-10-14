empty_list = []
grocery_list = ["bread", "apples", "ice cream", 42, True]

#ordered
list_of_buyers = ["Sam", "Adele", "Melvin", "Lilly", "Matt"]
list_of_buyers.append("Jake")
print(list_of_buyers)

list_of_buyers = ["Sam", "Adele", "Melvin", "Lilly", "Matt", "Adele", "Adele"]
print(list_of_buyers.count("Adele"))
list_of_buyers.insert(0, "Tim")
print(list_of_buyers)

list_of_buyers.sort()
print(list_of_buyers)

empty_dictionary = {}
car_dictionary = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": "1964"
    }
car_dictionary.pop("Model")
print(car_dictionary)

user_list = []

user_list.append({
    "Username": "Sam",
    "Password": "12345PasswordDogsRule!",
    "Email":""
})
