import json
import csv


# Definition of class 
class DataTable:
    def __init__(self, data_path):
        self.data_path = data_path
        self.item = []
        self.category = []
        self.price = []
        if self.data_path.endswith('.json'):
            self.from_json(self.data_path)
        elif self.data_path.endswith('.csv'):
            self.from_csv()


    def from_json(self, data_path):
        """
        Loads data from a JSON file and populates the instance attributes.
        

        Args:
            data_path (str): The path to the JSON file.

        Returns:
            list: The data loaded from the JSON file.
        """
        with open(self.data_path, 'r') as file:
            data = json.load(file)

        for row in data:
            self.item.append(row['item'])
            self.category.append(row['category'])
            self.price.append(row['price'])
    
    def from_csv(self, data_path):
        """
        Loads data from a CSV file and populates the instance attributes.

        Args:
            data_path (str): The path to the CSV file.

        Returns:
            list: The data loaded from the CSV file.
        """
        with open(self.data_path, 'r') as file:
            data = csv.reader(file)
            for row in data:
                # print(row)
                self.item.append(row[0])
                self.category.append(row[1])
                self.price.append(row[2]) 
            return data
            
# Create DataTable object
data_path = 'grocery_list.json'
table = DataTable(data_path)

print(table.item)
print(table.category)
print(table.price)



# import json
# import csv

# # Definition of class 
# class DataTable:

#     def __init__(self, data_path):
#         self.data_path = data_path
#         self.item = []
#         self.category = []
#         self.price = []
#         self.load_data()

#     def load_data(self):
#         with open(self.data_path, 'r') as file:
#             # data = json.load(file)
#             data = csv.reader(file)
#         # self.item = [1,2,3]
#         # self.category = [2,3,4]
#         # self.price = [4,5,6]
#             for items in data:
#                 # print(items)
#                 if len(items) >= 3:
#                     self.item.append(items[0])
#                     self.category.append(items[1])
#                     self.price.append(items[2]) 
            
# # Create DataTable object
# # data_path = 'grocery_list.json'
# data_path = 'grocery_list.csv'
# table = DataTable(data_path)

# print(table.item)
# print(table.category)
# print(table.price)
