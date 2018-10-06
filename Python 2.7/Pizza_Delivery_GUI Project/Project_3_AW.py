

'''--------------------------------------------------
Anthony Willmore
Phillip Austin
IS 340
Dec 9 2014
--------------------------------------------------'''

from Tkinter import *
import tkMessageBox
from time import gmtime, strftime


Window = Tk() # Creates User Window
Window.title('Super Pizza Bros')

# Pizza Sizes and Credit Cards (String Variables)

Pizza_Size = StringVar() 
Card_Type  = StringVar()

# Pizza Toppings (Integer Variables)

Pepperoni   = IntVar()
Sausage     = IntVar()
Olives      = IntVar()
Onions      = IntVar()
Pineapple   = IntVar()
Bell_Pepper = IntVar()

# Row 1 Pizza Image

Pizza_image = PhotoImage(file = "pizza-icon.gif")
Pizza_label = Label(Window, image = Pizza_image)
Pizza_label.grid(row = 1, column = 0, columnspan = 4)

# Row 2 Customer Name Input box

Customer_field = Label(Window, text = 'Customer Name:')
Customer_field.grid (row = 2, column = 0, sticky = E)
Customer_box = Entry(Window) 
Customer_box.grid(row = 2, column = 1, sticky = W)

# Row 3 Pizza Sizes

Small_Pizza = Radiobutton(Window, text = 'Small', variable = Pizza_Size, value = 'Small')
Small_Pizza.grid(row = 3, column = 0, sticky = W)

Medium_Pizza = Radiobutton(Window, text = 'Medium', variable = Pizza_Size, value = 'Medium')
Medium_Pizza.grid(row = 3, column = 1, sticky = W)

Large_Pizza = Radiobutton(Window, text = 'Large', variable = Pizza_Size, value = 'Large')
Large_Pizza.grid(row = 3, column = 2, sticky = W)
Large_Pizza.select()

# Row 4 Toppings

Toppings = Label(Window, text = 'TOPPINGS')
Toppings.grid(row = 4, column = 0, sticky = W, pady = 10 )

# Row 5 Pepperoni and Sausage Toppings

pepperoni = Checkbutton(Window, text = 'Pepperoni', variable = Pepperoni, onvalue = 1, offvalue = 0)
pepperoni.grid(row = 5, column = 0, sticky = W)

sausage = Checkbutton(Window, text = 'Sausage', variable = Sausage, onvalue = 1, offvalue = 0)
sausage.grid(row = 5, column = 1, sticky = W)


#Row 6 Olives and Onions Toppings

olives = Checkbutton(Window, text = 'Olives', variable = Olives, onvalue = 1, offvalue = 0)
olives.grid(row = 6, column = 0, sticky = W)

onions = Checkbutton(Window, text = 'Onions', variable = Onions, onvalue = 1, offvalue = 0)
onions.grid(row = 6, column = 1, sticky = W)

#Row 7 Pineapple and Bell Pepper Toppings

pineapple = Checkbutton(Window, text = 'Pineapple', variable = Pineapple, onvalue = 1, offvalue = 0)
pineapple.grid(row = 7, column = 0, sticky = W)

bellpepper = Checkbutton(Window, text = 'Bell Pepper', variable = Bell_Pepper, onvalue = 1, offvalue = 0)
bellpepper.grid(row = 7, column = 1, sticky = W)

#Row 8 Credit Card Payment
Credit_Label = Label(Window, text = 'CREDIT CARD PAYMENT')
Credit_Label.grid(row = 8, column = 0, sticky = W ,pady = 10, )

#Row 9 Types of Credit Cards

Visa = Radiobutton(Window, text = 'Visa', variable = Card_Type, value = 'Visa')
Visa.grid(row = 9, column = 0, sticky = W)
Visa.select()

MasterCard = Radiobutton(Window, text = 'Master Card', variable = Card_Type, value = 'Master Card')
MasterCard.grid(row = 9, column = 1, sticky = W)

AmericanExpress = Radiobutton(Window, text = 'American Express', variable = Card_Type, value = 'American Express')
AmericanExpress.grid(row = 9, column = 2, sticky = W)

#Function for submit button: After order is submitted, its sent to order.txt

def writeToFile():
    file = open('Orders.txt','a')
    if Customer_box.get() == '':    #Makes sure a name is tyepd in
        tkMessageBox.showinfo('Error', 'Please enter a name in the field.' )
        return
    file.write('Customer Name: %s\n' % Customer_box.get())
    file.write('Size: %s\n' % Pizza_Size.get())
    if Pepperoni.get()   == 1:
        file.write('      Pepperoni\n')
    if Sausage.get()     == 1:
        file.write('      Sausage\n')
    if Olives.get()      == 1:
        file.write('      Olives\n')
    if Onions.get()      == 1:
        file.write('      Onion\n')
    if Pineapple.get()   == 1:
        file.write('      Pineapple\n')
    if Bell_Pepper.get() == 1:
        file.write('      Bell Pepper\n')
    file.write('Card: %s\n' % Card_Type.get())
    file.write(strftime("Time: %x %I:%M %p\n",))
    file.write('========================================================\n')
    tkMessageBox.showinfo('Thanks for placing an order', 'Your order will be prepared and made promptly.')
    file.flush()
    file.close()
    resetFields()
    

#Function for Clear button: When you hit the 'Clear' button, it resets toppings, size, and credit card.

def resetFields():
    Customer_box.delete(0,END)
    pepperoni.deselect()
    sausage.deselect() 
    olives.deselect()
    onions.deselect()
    pineapple.deselect()
    bellpepper.deselect()
    Large_Pizza.select()
    Visa.select()

#ROW 10 Clear Button and Submit Button

Clear_Button = Button(Window, text= 'Clear', command = resetFields)
Clear_Button.grid(row = 10 ,column = 0, sticky = E, pady = 15 )

Submit_Button = Button(Window, text= 'Submit', command= writeToFile)
Submit_Button.grid(row = 10 ,column = 2 ,sticky = W)

#Keeps looping the Window

Window.mainloop() 
