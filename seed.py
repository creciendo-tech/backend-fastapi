import csv

# List of dictionaries with item data
items = [
  {"id": 1, "title": "Item 1", "description": "Description 1", "price": 10.00},
  {"id": 2, "title": "Item 2", "description": "Description 2", "price": 20.00},
  {"id": 3, "title": "Item 3", "description": "Description 3", "price": 30.00},
  {"id": 4, "title": "Item 4", "description": "Description 4", "price": 40.00},
  {"id": 5, "title": "Item 5", "description": "Description 5", "price": 50.00},
  {"id": 6, "title": "Item 6", "description": "Description 6", "price": 60.00}, 
  {"id": 7, "title": "Item 7", "description": "Description 7", "price": 70.00},
  {"id": 8, "title": "Item 8", "description": "Description 8", "price": 80.00},
  {"id": 9, "title": "Item 9", "description": "Description 9", "price": 90.00},
  {"id": 10, "title": "Item 10", "description": "Description 10", "price": 100.00}
]

# Column names for CSV file
headers = ["id", "title", "description", "price"]

# Open CSV file for writing
with open('data.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames=headers)

  # Write headers
  writer.writeheader()

  # Write data rows
  writer.writerows(items)
