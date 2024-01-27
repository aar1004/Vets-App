# WhatsApp contact list
contacts = [
    {
        "name": "john",
        "phone": "86995 40359",
        "conversations": ["hi", "hello", "this is awesome day", "lets go and play"],
    },
    {
        "name": "fionna",
        "phone": "86995 40378",
        "conversations": ["hola", "whats up", "i m good", "hows ur day?"],
    },
    {
        "name": "george",
        "phone": "86995 47378",
        "conversations": ["hila", "whats up", "i m good", "hows ur day?"],
    },
]


search_keyword = input("enter keyword to search...")
print("search_keyword", search_keyword)

for contact in contacts:
    # if (
    #     contact["name"].lower().__contains__(search_keyword.lower())
    #     or contact["phone"].find(search_keyword >= 0)
    #     # or contact["conversations"].lower().__contains__(search_keyword.lower())
    # ):  # or  if contact["name"].lower().find(search_keyword.lower()>=0): it will work the same
    #     print(contact)
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")

    if contact["conversations"].lower().__contains__(search_keyword.lower()):
        print(contacts)
