import json

data = {
    "Name1" : " ",
    "Total_count": " ",
    "Accuracy" : " "
}

Name = input("Name: ")
# file = open("test.json", "r")
with open("test.json", "r") as file:
    texts = json.load(file)
if Name in texts:
    with open("test.json", "r") as file:
        Total_Count = (texts[Name]["Total_Count"])
        Accuracy = (texts[Name]["Accuracy"])
        data.update({"Name1":Name})
        data.update({"Total_count": Total_Count})
        data.update({"Accuracy": Accuracy})
elif Name not in texts:
    with open("test.json", "w")as f:
        texts[Name] = {"Total_Count": "0", "Accuracy": "0%"}
        json.dump(texts,f) 
print(data)


# for line, text in enumerate(texts):
#     lines = len(texts)
#     while data == -1:
#         data = text.find(Name)
#         count += 1
#         if data != -1:
#             print(count)
#             print("Name located")
#         elif count == lines:
#             print("ERROR")
#         else:
#             break
