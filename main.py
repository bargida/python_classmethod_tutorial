import json
import csv

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
            # data = json.load(file)
            data = csv.reader(file)
        # self.item = [1,2,3]
        # self.category = [2,3,4]
        # self.price = [4,5,6]
            for items in data:
                # print(items)
                if len(items) >= 3:
                    self.item.append(items[0])
                    self.category.append(items[1])
                    self.price.append(items[2]) 
            
# Create DataTable object
# data_path = 'grocery_list.json'
data_path = 'grocery_list.csv'
table = DataTable(data_path)

print(table.item)
print(table.category)
print(table.price)

