import json

# Sample data
person = {
    "name": "Jerry Doe",
    "age": 29,
    "city": "Berlin"
}

# Writing JSON to a file
with open('person.json', 'w') as file:
    json.dump(person, file)

print("JSON data has been stored in 'person.json'")