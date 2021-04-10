import sqlite3


# Creating Database to Fetch Product Details from

conn = sqlite3.connect('Product_List.db')

c = conn.cursor()

c.execute("""CREATE TABLE product_list(
    product_code integer,
    product_name text,
    product_cost real
    )""")

conn.commit()

conn.close()