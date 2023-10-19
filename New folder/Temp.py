import json

name = input("Name: ")
total_count = input("Count: ")
accuracy = input("accuracy: ")

data = {
    "Name" : name,
    "Total_Count" : total_count,
    "Accuracy" : accuracy,
}

with open("test.json", "a") as f:
    json.dump(data, f) 
    json.dump("/n", f)

with open("test.json", "r") as f:
    read = json.load(f)
    name = read["Name"]
    print(name) 