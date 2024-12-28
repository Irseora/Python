import json

# Loading ----------------------------------------------------------------------

def LoadData(self):
    with open('data.json', 'r') as file:
        data = json.load(file)


def LoadTodo(self, data):
    for i in data['todo_list']:
        a

# Saving -----------------------------------------------------------------------

def SaveData(self):
    with open('data.json', 'w') as file:
        data = json.dump(file)