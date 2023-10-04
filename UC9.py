contact_list = {
    "Samuel": {"phone": 996796759, "email": "samuzica68@gmail.com"},
    "Gabriel": {"phone": 987960801, "email": "bielssouz0@gmail.com"},
}

# Dictionary
print(f"{contact_list}\n")

# Display information for the chosen contact
print(list(contact_list.keys())[0])
print(contact_list["Samuel"])

# Add new contacts
contact_list["João"] = {"phone": 932478325, "email": "joaozinho333@gmail.com"}

print(contact_list)

# Modify values
contact_list["Gabriel"]["phone"] = 933333333
print(contact_list)

# Delete an entry
del contact_list["João"]
print(contact_list)

# Reorganize entries
reorganized_dictionary = sorted(contact_list)
print(reorganized_dictionary)
