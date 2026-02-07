import json

# Definition of class 
class DataTable:

    def __init__(self, data_path):
        self.data_path = data_path
        self.item = []
        self.category = []
        self.price = []
        self.load_data()


    def load_data(self):
        with open(self.data_path, 'r') as file:
            data = json.load(file)
        self.item = [1,2,3]
        self.category = [2,3,4]
        self.price = [4,5,6]

        return data



        


# Create DataTable object
data_path = 'grocery_list.json'
table = DataTable(data_path)

print(table.item)
print(table.category)
print(table.price)

