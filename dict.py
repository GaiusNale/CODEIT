phonebook = {
    "Hozier":"Profession: Singer\nAge: 32\nNationality: Ireland",
}

phonebook["David"] = "Shepherd"

print (phonebook)

del phonebook["Hozier"]

print (phonebook)

phonebook["David"] = "Banker"

print(phonebook)

if "David" in phonebook:
    print ("How did he get in there?")

animal_sounds = {
    "dog":"woof",
    "cat":"meow",
    "cow":"moo",
    "sheep":"baa",
    "horse":"neigh"
}