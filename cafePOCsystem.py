#My 1st python project

import os
os.system("cls")            #clrscreen
from os import startfile    #for opening dishes and member files  
import tkinter as tk
from tkinter import messagebox

sides = {}
mains = {}
beverages = {} 

#sides.txt to sides dict
with open ("sides.txt") as f:
    for line in f:
        (key, value) = line.rstrip("\n").split(":")             #rstrip to eliminate \n at end of lines
        sides[key] = value

#mains.txt to mains dict
with open ("mains.txt") as f:
    for line in f:
        (key, value) = line.rstrip("\n").split(":")             
        mains[key] = value

#beverages.txt to beverages dict
with open ("beverages.txt") as f:
    for line in f:
        (key, value) = line.rstrip("\n").split(":")             
        beverages[key] = value

#sides, mains and beverages dict combine into foods dict
foods = {}
for food in sides, mains, beverages:
    for key, value in food.items():               
        foods.setdefault(key, []).append(value)

#Create window "CAFE"
def main_window():
    global window
    window = tk.Tk()
    window.geometry("470x680")
    window.title("CAFE")
    window.config(bg="#2b5693")
    homePage()

#destroy frame 1 and display original frame(homepage)
def frame1_to_Home():
    frame1.destroy()
    homePage()

#destroy frame 1 and display original frame(homepage)
def frame2_to_Home():
    frame2.destroy()
    homePage()

def cart_to_order():
    frame3.destroy()

def checkout_to_order():
    frame4.destroy()
    frame3.destroy()

def search_to_home():
    frame5.destroy()

#destroy adminstrator page 
def frame6_to_Home():           
    frame6.destroy()

#Display menu from dictionaries
def displayMenu():
    global frame1
    frame1 = tk.Frame(window, bg="#2b5693")
    frame1.grid(row=0, column=0)
    frame.destroy()
    tk.Label(frame1, text = "TODAY'S MENU\n", bg="#2b5693", fg="white", font=14).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame1, text = "SIDES:", bg="#2b5693", fg="white", font=14).grid(row=1, column=0, padx=5, pady=5)
    for s, side in enumerate(sides, start=1):
        tk.Label(frame1, text = (f"{s}.\t{side}:\t{sides[side]}"), bg="#2b5693", fg="white", font=14).grid(row=s+1, column=0)
    tk.Label(frame1, text = "\nMAINS:", bg="#2b5693", fg="white", font=14).grid(padx=5, pady=5)
    for m, main in enumerate(mains, start=s+1):
        tk.Label(frame1, text = (f"{m}.\t{main}:\t{mains[main]}"), bg="#2b5693", fg="white", font=14).grid(row=m+2, column=0)                    #rows +2 for "MAINS" label
    tk.Label(frame1, text = "\nBEVERAGES:", bg="#2b5693", fg="white", font=14).grid(padx=5, pady=5)
    for b, beverage in enumerate(beverages, start=m+1):
        tk.Label(frame1, text = (f"{b}.\t{beverage}:\t{beverages[beverage]}"), bg="#2b5693", fg="white", font=14).grid(row=b+3, column=0)        #rows +2 for "MAINS"and "BEVERAGES" labels
    tk.Button(frame1, text="Start Order", width="18", command=order).grid()
    tk.Button(frame1, text="Return to home page", width="18", command=frame1_to_Home).grid()

#order page
def order():
    global frame2
    global sideqtys
    global mainqtys
    global beverageqtys
    sideqtys = []       #list for side dish spinbox
    mainqtys = []       #list for main dish spinbox
    beverageqtys = []   #list for beverage spinbox
    frame2 = tk.Frame(window, bg="#2b5693")
    frame2.grid(row=0, column=0)
    frame2.place(height="1200", width="500")
    frame1.destroy()    #destroy display menu frame
    tk.Label(frame2, text = "TODAY'S MENU\n", bg="#2b5693", fg="white", font=14).grid(row=0, column=0, padx=5, pady=5)
    tk.Label(frame2, text = "SIDES:", bg="#2b5693", fg="white", font=14).grid(row=1, column=0, padx=5, pady=5)
    tk.Label(frame2, text = "QUANTITY:", bg="#2b5693", fg="white", font=14).grid(row=1, column=1, padx=5, pady=5)
    for s, side in enumerate(sides, start=1):
        tk.Label(frame2, text = (f"{s}.\t{side}:\t{sides[side]}"), bg="#2b5693", fg="white", font=14).grid(row=s+1, column=0)
        sideqty = tk.Spinbox(frame2, from_=0, to=30, width=5, state="readonly")           #create sideqty variable to enable get() function in quantity()
        sideqty.grid(row=s+1, column=1, padx=4, pady=4)
        sideqtys.append(sideqty)
    tk.Label(frame2, text = "\nMAINS:", bg="#2b5693", fg="white", font=14).grid(padx=5, pady=5)
    for m, main in enumerate(mains, start=s+1):
        tk.Label(frame2, text = (f"{m}.\t{main}:\t{mains[main]}"), bg="#2b5693", fg="white", font=14).grid(row=m+2, column=0)                #rows +2 for "MAINS" label
        mainqty = tk.Spinbox(frame2, from_=0, to=30, width=5, state="readonly")           #create mainqty variable to enable get() function in quantity()
        mainqty.grid(row=m+2, column=1, padx=4, pady=4)
        mainqtys.append(mainqty)
    tk.Label(frame2, text = "\nBEVERAGES:", bg="#2b5693", fg="white", font=14).grid(padx=5, pady=5)
    for b, beverage in enumerate(beverages, start=m+1):
        tk.Label(frame2, text = (f"{b}.\t{beverage}:\t{beverages[beverage]}"), bg="#2b5693", fg="white", font=14).grid(row=b+3, column=0)    #rows +2 for "MAINS"and "BEVERAGES" labels
        beverageqty = tk.Spinbox(frame2, from_=0, to=30, width=5, state="readonly")       #create beverageqty variable to enable get() function in quantity()
        beverageqty.grid(row=b+3, column=1, padx=4, pady=4)     
        beverageqtys.append(beverageqty)
    tk.Button(frame2, text="Add to cart", width="18", command=addToCart).grid()
    tk.Button(frame2, text="Reset", width="18", command=resetOrder).grid()
    tk.Button(frame2, text="Return to home page", width="18", command=frame2_to_Home).grid()  

#message box that pops up when click add to cart button
def addToCart():
    msgBox = tk.messagebox.askquestion ('Go to cart', 'Do you want to add to cart?', icon = 'warning')
    if msgBox == "yes":
        goToCart()      #and show cart pages

#store food quantity ordered
def quantity():
    temp = []
    foods_pxList = []                       #list of food and price, item eg. --> [french fries, $2.00]
    for key, value in foods.items():        #making food{} into list-->foods_pxList
        temp = [key, value]     
        foods_pxList.append(temp)
    foodqtys = []                           #list that store all dishes quantity
    for sideqty in sideqtys:
        foodqtys.append(sideqty.get())      #append all side dishes' spinbox values into foodqtys list
    for mainqty in mainqtys:
        foodqtys.append(mainqty.get())      #append all main dishes' spinbox values into foodqtys list
    for beverageqty in beverageqtys:
        foodqtys.append(beverageqty.get())  #append all beverages' spinbox values into foodqtys list

    #create dictionary of food dish and quantity{food dish: qty}
    dish_list = []                          #list to store all food dishes
    for key in foods:
        dish_list.append(key)
    global dish_qty_dict
    dish_qty_dict = dict(zip(dish_list, foodqtys))

#clear the order and refresh order page
def resetOrder():                           
    frame2.destroy()
    order()

#cart page
def goToCart():
    global frame3
    frame3 = tk.Frame(window)
    frame3.grid(row=0, column=0)
    frame3.place(height="800", width="500")
    quantity()
    tk.Label(frame3, text = "The orders in your CART:\n", fg="green", font=14).grid(row=0, column=0)
    tk.Label(frame3, text = "DISH\tQUANTITY:", fg="green", font=14).grid(row=1, column=0)
    tk.Label(frame3, text = "UNIT PRICE:", fg="green", font=14).grid(row=1, column=1)
    tk.Label(frame3, text = "SUB_TOTAL:", fg="green", font=14).grid(row=1, column=2)     #showing dish unit px times qty
    global dish_qty_list
    dish_qty_list = []
    global dish_unit_px_list
    dish_unit_px_list = []
    global r
    r = 2         #for .grid(row). +1 with every loop
    for key in dish_qty_dict:
        if int(dish_qty_dict[key]) > 0:
            tk.Label(frame3, text = (f"{key}\tx{dish_qty_dict[key]}\t"), font=14).grid(row=r, column=0)  #display dish  x(qty)
            dish_qty_list.append(dish_qty_dict[key])
            dish_ordered = key
            for food in foods:
                if food == dish_ordered:
                    dish_unit_px = str(foods[food])  
                    dish_unit_px_splice = dish_unit_px[2:-2]                                             #[2:-2] to remove sq bracket and ''
                    tk.Label(frame3, text = (f"{dish_unit_px_splice}"), font=14).grid(row=r, column=1)   #display dish unit px
                    dish_unit_px_list.append(dish_unit_px_splice)
                    r += 1
    totalPrice()
    s = 2       #row counter for subtotal px
    for x in totalPx_list:
        y = "{:.2f}".format(x)
        tk.Label(frame3, text = (f"${y}"), font=14).grid(row=s, column=2)                       #display all subtotal px beside dish unit px
        s += 1
    tk.Button(frame3, text = "Change order", command=cart_to_order, font=14).grid(row=r+2, column=0)     #row is r+2, bcos total px's row is r+1
    tk.Button(frame3, text = "Check Out", command=checkingOut, font=14).grid(row=r+2, column=1)

#message box that pops up when check out button clicked
def checkingOut():
    msgBox = tk.messagebox.askquestion ("Checking out", "Do you want to check out?", icon = "warning")
    if msgBox == "yes":
        checkOut()                                                                              #and show check out page

#checkout page
def checkOut():
    global frame4
    frame4 = tk.Frame(window)
    frame4.grid(row=0, column=0)
    frame4.place(height="900", width="500")
    quantity()
    tk.Label(frame4, text = "Checking Out:\n", fg="green", font=14).grid(row=0, column=0)
    tk.Label(frame4, text = "DISH\tQUANTITY:", fg="green", font=14).grid(row=1, column=0)
    tk.Label(frame4, text = "SUB_TOTAL:", fg="green", font=14).grid(row=1, column=1)
    global dish_qty_list
    dish_qty_list = []
    global dish_unit_px_list
    dish_unit_px_list = []
    global r
    r = 2         #for .grid(row). +1 with every loop
    for key in dish_qty_dict:
        if int(dish_qty_dict[key]) > 0:
            tk.Label(frame4, text = (f"{key}\tx{dish_qty_dict[key]}\t"), font=14).grid(row=r, column=0)  #display dish  x(qty)
            dish_qty_list.append(dish_qty_dict[key])
            dish_ordered = key
            for food in foods:
                if food == dish_ordered:
                    dish_unit_px = str(foods[food])  
                    dish_unit_px_splice = dish_unit_px[2:-2]                 #[2:-2] to remove sq bracket and ''
                    tk.Label(frame3, text = (f"{dish_unit_px_splice}"), font=14)      #no need to show for check out
                    dish_unit_px_list.append(dish_unit_px_splice)
                    r += 1
    global totalPx_list
    totalPx_list = []                                                        #list of total price of each dish
    for x, y in zip(dish_qty_list, dish_unit_px_list):
        z = y[1:]                                                            #get rid of $
        total_unit_dish_px = (int(x))*(eval(z))                              #dish qty times dish unit px to get total px for each dish
        totalPx_list.append(total_unit_dish_px)                
    global totalPx
    totalPx = "{:.2f}".format(sum(totalPx_list))                             #2dp for total price
    tk.Label(frame4, text = "TOTAL PRICE:", bg="#737375", fg="white", font=14).grid(row=r+1, column=0, sticky="w", padx=8, pady=8)
    tk.Label(frame4, text = (f"${totalPx}"), bg="#737375", fg="white", font=14).grid(row=r+1, column=1, padx=8, pady=8)
    s = 2       #row counter for subtotal px
    for x in totalPx_list:
        y = "{:.2f}".format(x)
        tk.Label(frame4, text = (f"${y}"), font=14).grid(row=s, column=1)             #display all subtotal px beside dish unit px
        s += 1
    tk.Button(frame4, text = "Change order", command=checkout_to_order).grid(row=r+2, column=0) 
    tk.Button(frame4, text = "Make payment", command=makePayment_msg).grid(row=r+2, column=1)

#calc total price and display it
def totalPrice():
    global totalPx_list
    totalPx_list = []                                      #list of total price of each dish
    for x, y in zip(dish_qty_list, dish_unit_px_list):
        z = y[1:]     #get rid of $
        total_unit_dish_px = (int(x))*(eval(z))            #dish qty times dish unit px to get total px for each dish
        totalPx_list.append(total_unit_dish_px)                
    global totalPx
    totalPx = "{:.2f}".format(sum(totalPx_list))           #2dp for total price
    tk.Label(frame3, text = "TOTAL PRICE:", bg="#737375", fg="white", font=14).grid(row=r+1, column=1, sticky="w", padx=8, pady=8)
    tk.Label(frame3, text = (f"${totalPx}"), bg="#737375", fg="white", font=14).grid(row=r+1, column=2, padx=8, pady=8)

#msg box that pops up when user click yes at the checkout msgbox
def makePayment_msg():
    msgBox = tk.messagebox.showinfo("Make Payment", "Please make your payment of "+(f"${totalPx}") +" at the counter.\nThank you and have a nice day:)")
    if msgBox == "ok":
        window.destroy()

#search page
def searchMenu():
    global frame5
    frame5 = tk.Frame(window)
    frame5.grid(row=0, column=0)
    frame5.place(height="900", width="500")
    tk.Label(frame5, text = "Enter your search: ").grid(row=0, column=0)
    global searchBar
    searchBar = tk.Entry(frame5)
    searchBar.grid(row=1, column=0)
    searchBar.bind("<Return>", getSearch)       #bind enter key: enter key also activates login()
    tk.Button(frame5, text = "ENTER", command=getSearch, font=14).grid(row=1, column=1)
    tk.Button(frame5, text="Clear", command=clearSearch, font=14).grid(row=2, column=1)
    tk.Button(frame5, text="Return to home page", command=search_to_home, font=14).grid(row=2, column=0, sticky="w")  

#display of search results
def getSearch(event=None):               #bind() passes a variable, whereas Button.command doesn't, so need getSearch() to accept an optional parameter, and then ignore it
    search = (searchBar.get()).lower()   #.lower for instances where user input in uppercase
    searchBar.delete(0, 'end')           #clear input field when clicked ENTER
    if len(search) == 0:
            tk.messagebox.showwarning("Null input", "No input registered!\nDisplaying Today's Menu.")
    keyword = dict(filter(lambda item: search in item[0], foods.items()))
    if len(keyword) > 0:
        tk.Label(frame5, text = "\nWe have the following dishes!\n", fg="green", font=14).grid()
        for i, key in enumerate(keyword, start=1):
            valueSlice = (str(keyword[key])[1:-1])                     #to remove sq bracket
            result = (f"{i}.\t{key}:\t{(valueSlice[1:-1])}")           #[1:-1] to remove quotes       
            dishSearch = tk.Label(frame5, text = result, fg="green")
            dishSearch.grid()
    else:
        tk.Label(frame5, text = (f"\nSorry! We do not serve {search}!\n"), fg="red", font=14).grid()

#clear the search screen by destroying frame and running search func again
def clearSearch():              
    frame5.destroy()
    searchMenu()

#login screen that ask for UN and PW inputs
def admin():
    global login_screen
    login_screen = tk.Toplevel(frame)
    login_screen.title("Admin Login")
    login_screen.minsize(250,180)
    login_screen.maxsize(250,180)

    global username
    global password
    global unInput
    global pwInput
    username = "admin"
    password = "cafe"
    
    tk.Label(login_screen, text="Username:", font=14).pack()
    unInput = tk.Entry(login_screen)
    unInput.pack()
    tk.Label(login_screen, text="", font=14).pack()  #empty row, just for row gap between UN and PW
    tk.Label(login_screen, text="Password:", font=14).pack()
    pwInput = tk.Entry(login_screen)
    pwInput.pack()
    pwInput.bind("<Return>",  login)        #bind enter key: enter key also activates login()
    tk.Label(login_screen, text="").pack()
    butt = tk.Button(login_screen, text="Login", command=login, font=14)
    butt.pack()
    butt.bind("<Return>",  login)
    
#login UN and PW validation
def login(event=None):          #bind() passes a variable, whereas Button.command doesn't, so need login() to accept an optional parameter, and then ignore it
    if unInput.get() == username:
        if pwInput.get() == password:
            superadmin()        #display superadmin page when UN and PW accepted
            login_screen.destroy() 
        else:
            msgBox_un = tk.messagebox.showwarning("Login error", "Password not recognised!")
            if msgBox_un == "ok":
                login_screen.destroy()  #to close login screen upon pressing ok
    else:
        msgBox_pw = tk.messagebox.showwarning("Login error", "Username not recognised!")  
        if msgBox_pw == "ok":
            login_screen.destroy()         

#open side dishes file
def sides_files():
    startfile("C:/Users/writeYourself/sides.txt")

#open main dishes file
def mains_files():
    startfile("C:/Users/writeYourself/mains.txt")

#open beverages file
def beverages_files():
    startfile("C:/Users/writeYourself/beverages.txt")

#open membership files
def member_files():
    startfile("C:/Users/writeYourself/members.txt")

#open instructions files
def instructions_files():
    startfile("C:/Users/writeYourself/README.txt")

#membership registration window
def register():
    global reg_screen
    reg_screen = tk.Toplevel(frame)
    reg_screen.title("Register")
    reg_screen.minsize(270,240)
    reg_screen.maxsize(270,240)

    global unReg
    global emailReg
    global pwReg
    tk.Label(reg_screen, text="Username:", font=14).pack()
    unReg = tk.Entry(reg_screen)
    unReg.pack()
    tk.Label(reg_screen, text="", font=14).pack()    #empty row, just for row gap 
    tk.Label(reg_screen, text="Email address:", font=14).pack()
    emailReg = tk.Entry(reg_screen)
    emailReg.pack()
    tk.Label(reg_screen, text="", font=14).pack()    #empty row, just for row gap 
    tk.Label(reg_screen, text="Password:", font=14).pack()
    pwReg = tk.Entry(reg_screen)
    pwReg.pack()
    pwReg.bind("<Return>",  register_member)          #bind enter key
    tk.Label(reg_screen, text="", font=14).pack()
    Rbutt = tk.Button(reg_screen, text="Register", command=register_member, font=14)
    Rbutt.pack()
    Rbutt.bind("<Return>",  register_member)

#get registration info and add to membership file
def register_member(event=None):
    unInfo = unReg.get()
    emailInfo = emailReg.get()
    pwInfo = pwReg.get()
    msgBox_reg = tk.messagebox.showinfo("Register", "Registration complete.\nCheck your email for any upcoming promotions!")
    if msgBox_reg == "ok":
        reg_screen.destroy()        #destroy reg screen, close it upon clicking ok button 
    mfile = open("members.txt","a") #append mode 
    mfile.write(f"\n{unInfo}\t\t{emailInfo}\t\t{pwInfo}") 
    mfile.close() 

#admin screen where admin can access files
def superadmin():
    global frame6
    frame6 = tk.Frame(window)
    frame6.grid(row=0, column=0)
    frame6.place(height="800", width="500")
    tk.Label(frame6, text = "Welcome Administrator!", fg="red", font=14).grid(row=0, column=0) 
    tk.Label(frame6, text="", font=14).grid()
    tk.Button(frame6, text = "Open side dishes files", width="18", command=sides_files, font=14).grid()
    tk.Button(frame6, text = "Open main dishes files", width="18", command=mains_files, font=14).grid()
    tk.Button(frame6, text = "Open beverages files", width="18", command=beverages_files, font=14).grid()
    tk.Button(frame6, text = "Open membership file", width="18", command=member_files, font=14).grid()
    tk.Button(frame6, text = "Open instructions file", width="18", command=instructions_files, font=14).grid()
    tk.Button(frame6, text = "Logout", command=frame6_to_Home, width="18", font=14).grid()

#Original frame that shows homepage
def homePage():
    global frame
    frame = tk.Frame(window,  bg="#2b5693")
    frame.grid(row=0, column=0)
    #_____LABELS_____
    tk.Label(frame, text="THE CAFE\nAUTOMATED MENU SYSTEM", font=("Roboto medium", 15), 
            fg="red", bg="#dee1e2").grid(row=0, column=0, columnspan=2, sticky="WE", padx=5, pady=10)

    tk.Label(frame, text="Display Today's Menu", fg="black", bg="#dee1e2", width="20", anchor="w", font=14).grid(row=1, column=0, sticky="E", padx=5, pady=10)

    tk.Label(frame, text="Search Menu", fg="black", bg="#dee1e2", width="20", anchor="w", font=14).grid(row=2, column=0, sticky="E", padx=5, pady=10)

    tk.Label(frame, text="Join Membership", fg="black", bg="#dee1e2", width="20", anchor="w", font=14).grid(row=3, column=0, sticky="E", padx=5, pady=10)

    tk.Label(frame, text="Join member to get future promotions!", fg="red", bg="#95AAC9", anchor="w", font=8).grid(row=4, column=0, sticky="E", padx=2, pady=3, columnspan=2)
    #_____BUTTONS_____
    tk.Button(frame, text="Go!", command=displayMenu, font=14).grid(row=1, column=1, sticky="w", padx=5, pady=10)    #Display today's menu button

    tk.Button(frame, text="Go!", command=searchMenu, font=14).grid(row=2, column=1, sticky="w", padx=5, pady=10)     #Search menu button

    tk.Button(frame, text="Go!", command=register, font=14).grid(row=3, column=1, sticky="w", padx=5, pady=10)       #Join membership button

    tk.Button(frame, text="Admin", command=admin, font=14).grid(row=5, column=2, sticky="w", padx=5, pady=10) 

    window.mainloop()                                                                                       #keep window constantly open

main_window()


