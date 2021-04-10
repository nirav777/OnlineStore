from tkinter import *

from Add_product_to_DB_maually_Function import *
from ReceiptWindow import *

# Creating Main Interface

root = Tk()
root.geometry("1100x600")
root.title("Grocery Store")
root["bg"] = "gray25"

main_Label = Label(root,
                   text="Online Grocery Store System",
                   font=("Arial", 25, "bold italic underline"),
                   bg="gold",
                   fg="black")
main_Label.grid(sticky="W", padx=25, pady=25)

# Label and Entry Widget

product_Code_Label = Label(root, text="Product Code: ", font=("Times", 15), bg="light yellow")
product_Code_Label.grid(row=1, column=0)

product_Code_Input = Entry(root, width=30, borderwidth=7)
product_Code_Input.grid(row=1, column=2, padx=10, pady=10)


# Function to Fetch Details of Product from Database and Display them in Main Interface

def display():
    recordID = product_Code_Input.get()
    conn = sqlite3.connect('Product_List.db')
    c = conn.cursor()
    c.execute("SELECT * FROM product_list WHERE oid = " + recordID)
    records = c.fetchall()
    for record in records:
        product_Name_Input.insert(0, record[1])
        product_Cost_Input.insert(0, record[2])

    conn.commit()
    conn.close()


# Button to Display Product Details

display_button = Button(root, text="DISPLAY PRODUCT DETAILS", font="Times", command=display, borderwidth=5,
                        bg="light yellow")
display_button.grid(row=1, column=3, padx=50)

# Labels and Entry Widgets

product_Name_Label = Label(root, text="Product Purchased: ", font=("Times", 15), bg="light yellow")
product_Name_Label.grid(row=2, column=0)

product_Name_Input = Entry(root, width=30, borderwidth=7)
product_Name_Input.grid(row=2, column=2, padx=10)

product_Cost_Label = Label(root, text="Product Cost: ", font=("Times", 15), bg="light yellow")
product_Cost_Label.grid(row=3, column=0)

product_Cost_Input = Entry(root, width=30, borderwidth=7)
product_Cost_Input.grid(row=3, column=2, padx=10, pady=10)

Quantity = Label(root, text="Quantity: ", font=("Times", 15), bg="light yellow")
Quantity.grid(row=4, column=0)

Quantity_Input = Entry(root, width=30, borderwidth=7)
Quantity_Input.grid(row=4, column=2, padx=10)


# Function for Calculating Total Amount of a Particular Product

def calculate():
    a = Quantity_Input.get()
    b = product_Cost_Input.get()
    c = float(a) * float(b)
    Total_Amount_Display.insert(0, c)


calculate_button = Button(root, text="CALCULATE", font="Times", command=calculate, borderwidth=5,
                          bg="light yellow")
calculate_button.grid(row=4, column=3, padx=50)

Total_Amount = Label(root, text="Total Amount of this Product: ", font=("Times", 15), bg="light yellow")
Total_Amount.grid(row=5, column=0)

Total_Amount_Display = Entry(root, width=30, borderwidth=7)
Total_Amount_Display.grid(row=5, column=2, padx=10, pady=10)


# Function for Adding the Product to User's Cart Database

def add_product_to_cart():
    conn = sqlite3.connect('Cart.db')
    c = conn.cursor()
    c.execute("INSERT INTO cart VALUES(:Product_Code, :Product_Name, :Amount, :Quantity )",
              {
                  'Product_Code': product_Code_Input.get(),
                  'Product_Name': product_Name_Input.get(),
                  'Amount': Total_Amount_Display.get(),
                  'Quantity': Quantity_Input.get()
              }
              )
    conn.commit()
    conn.close()

    product_Code_Input.delete(0, END)
    product_Cost_Input.delete(0, END)
    product_Name_Input.delete(0, END)
    Total_Amount_Display.delete(0, END)
    Quantity_Input.delete(0, END)


# Creating and Adding Buttons to the Main Interface

add_Product_button = Button(root, text="ADD TO CART", font="Times", command=add_product_to_cart, borderwidth=5,
                            bg="light yellow")
add_Product_button.grid(row=6, column=2)

bill_button = Button(root, text="DISPLAY BILL", font="Times", command=bill, borderwidth=5, bg="light yellow")
bill_button.grid(row=7, column=2, pady=10)

exit_app_button = Button(root, text="EXIT", font="Times", command=root.quit, borderwidth=5, bg="light yellow")
exit_app_button.grid(row=8, column=2)

admin_access_button = Button(root, text="ADMIN", font="Times", command=add_product_to_database, borderwidth=5,
                             bg="light yellow")
admin_access_button.grid(row=9, column=3, pady=10)

root.mainloop()
