import sqlite3


# Adding Few Products to the Product Fetching Database using SQL

conn = sqlite3.connect('Product_List.db')

c = conn.cursor()

# c.execute('''
#                 INSERT INTO product_list (product_code, product_name, product_cost)
#                 VALUES
#                 (1, "Bread", 30.50),
#                 (2, "Butter", 20.50),
#                 (3, "Jam", 50),
#                 (4, "Cheese Cube", 15),
#                 (5, "Cottage Cheese", 90),
#                 (6, "Cream", 69.90),
#                 (7, "Milk", 22.70),
#                 (8, "Curd", 40.30),
#                 (9, "Ghee", 70.20),
#                 (10, "Butter Milk", 100.50)
#                 ''')

conn.commit()

conn.close()
