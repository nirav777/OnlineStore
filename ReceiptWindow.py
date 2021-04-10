from tkinter import *
import sqlite3


# Receipt Generating Window

def bill():
    # Creating Receipt Window

    newWindow2 = Tk()
    newWindow2.title("RECEIPT")
    newWindow2.geometry("700x500")
    newWindow2["bg"] = "gray25"

    # Adding "Total Bill: " Label

    bill_Label = Label(newWindow2,
                       text="TOTAL BILL: ",
                       font=("Arial", 10, "bold italic underline"),
                       bg="gold",
                       fg="black")
    bill_Label.grid(sticky="W", padx=25, pady=10)

    # Function for Displaying Products in User's Cart and Amount of each Product

    def show():
        conn = sqlite3.connect('Cart.db')
        c = conn.cursor()
        c.execute("SELECT *, oid from cart")
        records = c.fetchall()

        # loop
        printRecord = ''
        printRecord2 = ''
        for record in records:
            printRecord = printRecord + record[1] + "\n"
            printRecord2 = printRecord2 + "₹ " + str(record[2]) + "\n"

        printLabel1 = Label(newWindow2, text=printRecord,
                            font=("Arial", 12, "bold"),
                            bg="gold",
                            fg="black")
        printLabel1.grid(row=2, column=1, columnspan=2)

        printLabel2 = Label(newWindow2, text=printRecord2,
                            font=("Arial", 12, "bold"),
                            bg="gold",
                            fg="black")
        printLabel2.grid(row=2, column=2, columnspan=2)

        conn.commit()
        conn.close()

    show()

    # Calculating and Printing the Total Bill

    def receipt():
        conn = sqlite3.connect('Cart.db')
        c = conn.cursor()
        c.execute("SELECT *, oid from cart")
        records = c.fetchall()

        # Loop
        # For Total Amount of Products

        totalAmount = 0.0
        for record in records:
            if record[2] == '':
                continue
            totalAmount = totalAmount + float(record[2])

        totalBill = totalAmount

        totalLabel = Label(newWindow2, text="Total Bill: " + "\t \t" + "₹ " + str(totalBill),
                           font=("Arial", 15, "bold"),
                           bg="gold",
                           fg="black")
        totalLabel.grid(row=3, column=1, columnspan=2)

        # For Total Product Count

        totalQuantity = 0
        for record in records:
            if record[3] == '':
                continue
            totalQuantity = totalQuantity + int(record[3])

        totalLabel = Label(newWindow2, text="Total Products Purchased: " + "\t" + str(totalQuantity),
                           font=("Arial", 15, "bold"),
                           bg="gold",
                           fg="black")
        totalLabel.grid(row=4, column=1, columnspan=2)

        conn.commit()
        conn.close()

    receipt()

    # Function for Deleting User's Cart Database

    def delete_cart():
        conn = sqlite3.connect('Cart.db')
        c = conn.cursor()
        for i in range(0, 20):
            c.execute("DELETE FROM cart WHERE Product_Code = " + str(i))
        conn.commit()
        conn.close()
        newWindow2.destroy()

    # Function for Printing Receipt

    def printReceipt():
        return

    # Taking Paid Input and Displaying Balance Value

    paidLabel = Label(newWindow2, text="Paid Amount: ", font=("Times", 15), bg="light yellow")
    paidLabel.grid(row=5, column=1)

    paidLabel_Input = Entry(newWindow2, width=30, borderwidth=7)
    paidLabel_Input.grid(row=5, column=2, padx=10, pady=15)

    balanceLabel = Label(newWindow2, text="Balance: ", font=("Times", 15), bg="light yellow")
    balanceLabel.grid(row=6, column=1)

    balanceLabel_Input = Entry(newWindow2, width=30, borderwidth=7)
    balanceLabel_Input.grid(row=6, column=2, padx=10)

    # Function for Calculating Balance

    def balanceCalculation():
        paid = float(paidLabel_Input.get())
        conn = sqlite3.connect('Cart.db')
        c = conn.cursor()
        c.execute("SELECT *, oid from cart")
        records = c.fetchall()

        # Loop

        total = 0.0
        for record in records:
            if record[2] == '':
                continue
            total = total + float(record[2])

        totalBill = total
        balance = paid - totalBill
        balanceLabel_Input.insert(0, balance)

    # Calculate Balance Button Creation

    calculateBalanceButton = Button(newWindow2, text="Calculate Balance", font="Times",
                                    command=balanceCalculation,
                                    borderwidth=5,
                                    bg="light yellow")
    calculateBalanceButton.grid(row=5, column=3, pady=15, padx=10)

    # "Thank You" Label

    thank_you_Label = Label(newWindow2,
                            text="THANK YOU AND VISIT AGAIN!",
                            font=("Arial", 12, "bold italic underline"),
                            bg="gold",
                            fg="black")
    thank_you_Label.grid(row=7, column=0, columnspan=4, pady=20)

    # Print Receipt, Delete Cart, Back Button Creation

    printReceipt_button = Button(newWindow2, text="PRINT RECEIPT", font="Times", command=printReceipt, borderwidth=5,
                                 bg="light yellow")
    printReceipt_button.grid(row=8, column=3, padx=10)

    delete_Cart_button = Button(newWindow2, text="DELETE CART", font="Times", command=delete_cart, borderwidth=5,
                                bg="light yellow")
    delete_Cart_button.grid(row=9, column=3, pady=15, padx=10)

    back_button = Button(newWindow2, text="BACK", font="Times", command=newWindow2.destroy, borderwidth=5,
                         bg="light yellow")
    back_button.grid(row=10, column=3, padx=10)
