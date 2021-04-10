from tkinter import *
import sqlite3


# Admin Adding Products to the Database Window

def add_product_to_database():

    # Creating New Window for Adding New Product to the Product Fetching Database

    newWindow = Tk()
    newWindow.title("Add New Product")
    newWindow.geometry("600x300")
    newWindow["bg"] = "gray25"

    # Adding Labels And Entry Widgets to New Window

    info_Label = Label(newWindow,
                       text="Add New Product Details Below: ",
                       font=("Arial", 10, "bold italic underline"),
                       bg="gold",
                       fg="black")
    info_Label.grid(sticky="W", padx=25, pady=10)

    product_Code_Label = Label(newWindow, text="Product Code: ", font=("Times", 15), bg="light yellow")
    product_Code_Label.grid(row=1, column=0)

    product_Code_Input = Entry(newWindow, width=30, borderwidth=7)
    product_Code_Input.grid(row=1, column=2, padx=10, pady=10)

    product_Name_Label = Label(newWindow, text="New Product Name: ", font=("Times", 15), bg="light yellow")
    product_Name_Label.grid(row=2, column=0)

    product_Name_Input = Entry(newWindow, width=30, borderwidth=7)
    product_Name_Input.grid(row=2, column=2, padx=10)

    product_Cost_Label = Label(newWindow, text="New Product Cost: ", font=("Times", 15), bg="light yellow")
    product_Cost_Label.grid(row=3, column=0)

    product_Cost_Input = Entry(newWindow, width=30, borderwidth=7)
    product_Cost_Input.grid(row=3, column=2, padx=10, pady=10)

    # Function for Adding New Product to the Product Fetching Database

    def add():
        conn = sqlite3.connect('Product_List.db')
        c = conn.cursor()
        c.execute("INSERT INTO product_list VALUES (:product_code, :product_name, :product_cost)",
                  {
                      'product_code': product_Code_Input.get(),
                      'product_name': product_Name_Input.get(),
                      'product_cost': product_Cost_Input.get()
                  }
                  )
        conn.commit()
        conn.close()
        product_Code_Input.delete(0, END)
        product_Name_Input.delete(0, END)
        product_Cost_Input.delete(0, END)

    # Creating Add and Exit Button

    addButton = Button(newWindow, text="ADD PRODUCT", font="Times", command=add, borderwidth=5, bg="light yellow")
    addButton.grid(row=4, column=2, pady=15)

    exitButton = Button(newWindow, text="BACK", font="Times", command=newWindow.destroy, borderwidth=5,
                        bg="light yellow")
    exitButton.grid(row=5, column=2)
