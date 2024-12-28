import json

# Loading ----------------------------------------------------------------------

def LoadData():
    with open('data.json', 'r') as file:
        data = json.load(file)

    

def LoadTodoList(data):
    

# def LoadTodo(self, data):
#     for entry in data['tasks']:
#         print(entry)
#     # for i in data['tasks']:
#     #     print(data)

# Saving -----------------------------------------------------------------------

def SaveData(self):
    with open('data.json', 'w') as file:
        data = json.dump(file)

LoadData()