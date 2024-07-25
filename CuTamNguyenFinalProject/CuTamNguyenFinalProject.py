'''
Author: Tam Nguyen Cu
Date Written: 07/20/2024
Assignments: Module 08 Final Project

This program creates an application GUI for ordering pizza online.
This GUI includes:
1/ Start page: the GUI's first page and cover page.
2/ Menu page: The menu page to view the pizza menu.
3/ Item page: The item detail page displays the item option before adding it to the cart.
4/ Orders page: Displays the user's orders.
5/ Cart page: Displays the user's selected item.

'''

# Import modules
import tkinter as tk
import random
import json
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime, timedelta

class PalacePizza:
    '''
    A class representing the Palace Pizza GUI application.
    Attributes:
        root: The main window of the application.
        cart: A list to store the user's selected items.
        orders: A list to store the user's orders.
        ACTION_ADD: A constant for adding an item to the cart.
        ACTION_REMOVE: A constant for removing an item from the cart.
    Methods:
        getData: Get data from the data file.
        startPage: The cover page of the application.
        mainPage: The main page of the application.
        menuPage: The menu page of the application.
        itemPage: The item detail page of the application.
        updateCart: Add or Remove items from the cart.
        cartPage: The cart page of the application.
        checkout: The checkout page of the application.
        placeOrder: Validate information and create orders.
        ordersPage: The orders page of the application.
        scrollableCanvas: Create a scrollable frame.
        clear_frame: Clear frame.
    '''
    def __init__(self):
        '''
        Initialize the PalacePizza class.
        Parameters:
            None
        Returns:
            None
        '''
        # Create GUI
        self.root = tk.Tk()
        self.root.title("Pizza Palace")
        self.root.geometry("1000x800")
        self.root.maxsize(1000, 800)
        
        # Create constants and variables
        self.cart = []
        self.orders = []
        self.ACTION_ADD = "add"
        self.ACTION_REMOVE = "remove"
    
        # Get data from the data file and call the start page
        self.getData()
        self.startPage()
        self.root.mainloop()
        
    def getData(self):
        '''
        Get data from the data file.
        Parameters:
            None
        Returns:
            None
        '''
        # Open the data file and load it
        file = open('data.json')
        data = json.load(file)
        self.menu = data['menu']
        
        self.menu_img = {
            "Pepperoni Pizza": ImageTk.PhotoImage(Image.open(f"images/Pizza_PEPPERONI.png").resize((100,100), Image.Resampling.LANCZOS)),
            "Cheese Pizza": ImageTk.PhotoImage(Image.open(f"images/Pizza_CHEESE.png").resize((100,100), Image.Resampling.LANCZOS)),
            "Supreme Pizza": ImageTk.PhotoImage(Image.open(f"images/Pizza_SUPREME.png").resize((100,100), Image.Resampling.LANCZOS)),
            "Garlic Bread": ImageTk.PhotoImage(Image.open(f"images/Sides_GarlicBread.png").resize((100,100), Image.Resampling.LANCZOS)),
            "Cheese Bread": ImageTk.PhotoImage(Image.open(f"images/Sides_CheeseBread.png").resize((100,100), Image.Resampling.LANCZOS)),
            "Breadsticks": ImageTk.PhotoImage(Image.open(f"images/Sides_Breadsticks.png").resize((100,100), Image.Resampling.LANCZOS)),
            "PEPSI": ImageTk.PhotoImage(Image.open(f"images/Drinks_Pepsi.png").resize((100,100), Image.Resampling.LANCZOS)),
            "MTN DEW": ImageTk.PhotoImage(Image.open(f"images/Drinks_MtnDew.png").resize((100,100), Image.Resampling.LANCZOS)),
            "Mug Root Beer": ImageTk.PhotoImage(Image.open(f"images/Drinks_MugRootBeer.png").resize((100,100), Image.Resampling.LANCZOS)),
        }
        
        file.close()
    
    def startPage(self):
        '''
        Create the start page of the application.
        Parameters:
            None
        Returns:
            None
        '''
        # Clear frame
        self.clear_frame(self.root)
        
        self.bg_img = ImageTk.PhotoImage(Image.open(f"images/start_bg.png").resize((1000,800)))
        tk.Label(self.root, image=self.bg_img).place(relheight=1, relwidth=1)
        
        tk.Label(self.root, text="Welcome to Palace Pizza!", 
                 fg="#ffffff", bg="#009246", font=('Helvetica 20 bold italic')).pack(side=tk.TOP, padx=10, pady=50)
        
        tk.Button(self.root, text="Start your orders here!", width=19, height=2, font=('Helvetica 15 bold'),
            command= self.mainPage).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def mainPage(self):
        '''
        Create the main page of the application.
        Parameters: 
            None
        Returns
            None
        '''
        self.clear_frame(self.root)
        
        # Create the navigation bar
        self.header = tk.Frame(self.root)
        self.header.pack(fill=tk.X)
        
        tk.Button(self.header, text="Pizza Palace", bd=0, font='Helvetica 20 bold italic',
                  command = self.startPage).pack(side=tk.LEFT,padx=20, pady=10)
        
        tk.Button(self.header, text="Menu", bd=0, font='Helvetica 18 bold',
                  command = self.menuPage).pack(side=tk.LEFT, padx=60, pady=10)
        
        tk.Button(self.header, text="Orders", bd=0, font='Helvetica 18 bold',
                  command = self.orderPage).pack(side=tk.LEFT, padx=60, pady=10)
        
        tk.Button(self.header, text="Cart", bd=0, font='Helvetica 18 bold',
                  command = self.cartPage).pack(side=tk.LEFT, padx=60, pady=10)

        # Create the body frame
        _, self.body = self.scrollableCanvas()
        self.menuPage()
        
    def menuPage(self):
        '''
        Create the menu page of the application.
        Parameters:
            None
        Returns:
            None
        '''
        # Clear the last frame
        self.clear_frame(self.body)
        
        # Generate menu item
        for item in self.menu:
            item_frame = tk.Frame(self.body)
            item_frame.pack(fill=tk.X, padx=5, pady=5)
            tk.Label(item_frame, image=self.menu_img[item['name']]).pack(side=tk.LEFT, padx=60)
            tk.Label(item_frame, text=f"{item['name']} - ${item['price']}", font='Helvetica 15').pack(side=tk.LEFT, padx=60)
            tk.Button(item_frame, text="GET STARTED", font='Helvetica 15',
                      command= lambda i=item: self.itemPage(i)).pack(side=tk.RIGHT)
            
    def itemPage(self, item):
        '''
        Create the item page of the application.
        Parameters:
            None
        Returns
            None
        '''
        self.clear_frame(self.body)
        
        # Get the item image
        self.item_img = ImageTk.PhotoImage(Image.open(f"{item['image_path']}").resize((200,200)))
        
        # Create item information and options
        tk.Label(self.body, image=self.item_img).pack(side=tk.LEFT, padx=50)
        tk.Label(self.body, text=f"{item['name']} - ${item['price']}", font='Helvetica 20 bold').pack(anchor=tk.W)
        
        # Check if the item has size option
        if item['sizes']:
            size_frame = tk.Frame(self.body)
            size_frame.pack(anchor=tk.W, pady=10)
            self.size_var = tk.StringVar(value="Large")
            tk.Label(size_frame, text="Sizes:", font='Helvetica 15').pack(anchor=tk.W)
            for size in item['sizes']:
                tk.Radiobutton(size_frame, text=size, variable=self.size_var, value=size, font='Helvetica 15').pack(side=tk.LEFT, padx=10)
        
        # Check if the item has crust options 
        if item['crust']:
            crust_frame = tk.Frame(self.body)
            crust_frame.pack(anchor=tk.W, pady=10)
            self.crust_var = tk.StringVar(value="Original Stuffed")
            tk.Label(crust_frame, text="Crust:", font='Helvetica 15').pack(anchor=tk.W)
            for cr in item['crust']:
                tk.Radiobutton(crust_frame, text=cr, variable=self.crust_var, value=cr, font='Helvetica 15').pack(side=tk.LEFT, padx=10)
        
        # Check if the item has toppings options   
        if item['toppings']:
            topping_frame = tk.Frame(self.body)
            topping_frame.pack(anchor=tk.W, pady=10)
            tk.Label(topping_frame, text="Toppings:", font='Helvetica 15').pack(anchor=tk.W)
            self.cb_var = {}
            for k, v in item['toppings'].items():
                self.cb_var[k]=tk.IntVar(value= v)
                tk.Checkbutton(topping_frame, text=k, variable=self.cb_var[k], font='Helvetica 15').pack(side=tk.TOP, anchor=tk.W)
       
        # Add to cart button 
        tk.Button(self.body, text="Add to Cart", font='Helvetica 15', 
                  command= lambda: self.updateCart(self.ACTION_ADD, item)).pack(side=tk.BOTTOM)
        
    def updateCart(self, action, item):
        '''
        Update the cart based on the action add or remove the item
        Parameters:
            action (str): The action to perform on the cart (ADD or REMOVE)
            item (dict): The item to be added or removed from the cart
        '''
        # If the action is add -> add to cart and display message
        # If the action is remove -> remove from cart and reload the cart page 
        if action == self.ACTION_ADD:
            self.cart.append(item)
            messagebox.showinfo("Added to cart", f"{item['name']} has been added to your cart.")
        elif action == self.ACTION_REMOVE:
            for cartItem in self.cart:
                if cartItem['name'] == item['name']:
                    self.cart.remove(cartItem)
                break
            self.cartPage()
        
    def cartPage(self):
        '''
        Create the cart page of the application.
        Parameters:
            None
        Returns:
            None
        '''
        self.clear_frame(self.body)
        
        # Calculate tax and total price
        subTotal = sum([item['price'] for item in self.cart])
        tax = subTotal * 0.07
        totalPrice = subTotal + tax
        
        # Create checkout button
        self.placeOrdBtn = tk.Button(self.body, text="Checkout", font='Helvetica 15 bold', bg="#009246", fg="#ffffff", width=30,command=self.checkout)
        self.placeOrdBtn.pack(side=tk.BOTTOM, anchor=tk.W, padx=30, pady=20)
        
        # If cart has items -> create item list
        # Else display empty cart message
        if self.cart:
            for item in self.cart:
                item_frame = tk.Frame(self.body)
                item_frame.pack(fill=tk.X, padx=5, pady=5)
                tk.Label(item_frame, image=self.menu_img[item['name']]).pack(side=tk.LEFT, padx=60)
                tk.Label(item_frame, text=f"{item['name']} - ${item['price']}", font='Helvetica 15').pack(side=tk.LEFT, padx=60)
                tk.Button(item_frame, text="Remove", font='Helvetica 15',
                        command= lambda i=item: self.updateCart(self.ACTION_REMOVE, i)).pack(side=tk.RIGHT)
        else:
            item_frame = tk.Frame(self.body)
            item_frame.pack(fill=tk.X, padx=5, pady=5)
            tk.Label(item_frame, text="Oh no! Your cart is empty.", font='Helvetica 15').pack(padx=350)
            self.placeOrdBtn.config(state=tk.DISABLED)
        
        # Display the total price and tax 
        tk.Label(self.body, text=f"Total Price: ${totalPrice:.2f}", font='Helvetica 20 bold').pack(side=tk.BOTTOM,anchor=tk.W, padx=30)
        tk.Label(self.body, text=f"Tax: ${tax:.2f}", font='Helvetica 15 bold').pack(side=tk.BOTTOM,anchor=tk.W, padx=30, pady=20)
        
    def checkout(self):
        '''
        Checkout process
        Parameters:
            None
        Returns:
            None
        '''
        self.clear_frame(self.body)
        
        # Create new frame
        infoFrame = tk.Frame(self.body)
        infoFrame.pack(side=tk.TOP, anchor=tk.CENTER, padx=300, pady=10)
        
        # Create checkout information form
        tk.Label(infoFrame, text="Your Information", font='Helvetica 20 bold').pack(side=tk.TOP, anchor=tk.N, padx=10, pady=5)
        tk.Label(infoFrame, text="Name:", font='Helvetica 12').pack(anchor=tk.W, padx=10)
        self.checkout_name_entry = tk.Entry(infoFrame)
        self.checkout_name_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(infoFrame, text="Address:", font='Helvetica 12').pack(anchor=tk.W, padx=10)
        self.checkout_address_entry = tk.Entry(infoFrame)
        self.checkout_address_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(infoFrame, text="Phone:", font='Helvetica 12').pack(anchor=tk.W, padx=10)
        self.checkout_phone_entry = tk.Entry(infoFrame)
        self.checkout_phone_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(infoFrame, text="Secure payment", font='Helvetica 20 bold').pack(anchor=tk.N, padx=10, pady=5)
        tk.Label(infoFrame, text="Credit Card Number:", font='Helvetica 12').pack(anchor=tk.W, padx=10)
        self.card_number_entry = tk.Entry(infoFrame)
        self.card_number_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(infoFrame, text="Expiration Date (MM/YY):", font='Helvetica 12').pack(anchor=tk.W, padx=10)
        self.card_expiry_entry = tk.Entry(infoFrame)
        self.card_expiry_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(infoFrame, text="CVV:", font='Helvetica 12').pack(anchor=tk.W, padx=10)
        self.card_cvv_entry = tk.Entry(infoFrame)
        self.card_cvv_entry.pack(fill=tk.X, padx=10, pady=5)
        
        # Place orders button
        tk.Button(infoFrame, text="Place Order", font='Helvetica 15 bold', bg="#e21216", fg="#ffffff", width=30,
                command=self.placeOrder).pack(anchor=tk.W, padx=10, pady=20)
    
    def placeOrder(self):
        '''
        Place the order and display a success message.
        Parameters:
            None
        Returns:
            None
        '''
        # Get entry data
        name = self.checkout_name_entry.get()
        address = self.checkout_address_entry.get()
        phone = self.checkout_phone_entry.get()
        card_number = self.card_number_entry.get()
        card_expiry = self.card_expiry_entry.get()
        card_cvv = self.card_cvv_entry.get()

        # Empty validation
        if not name or not address or not phone or not card_number or not card_expiry or not card_cvv:
            messagebox.showwarning("Missing Information!", "Please fill in all the information.")
            return
        
        # Phone number length validation
        if len(phone) != 10:
            messagebox.showwarning("Invalid Information!", "Invalid phone number! Please enter a valid phone number.")
            return
        
        # Card number length validation
        if len(card_number) < 15:
            messagebox.showwarning("Invalid Information!", "Invalid credit card number! Please enter a valid credit card number.")
            return
        
        # Expiration date validation
        expiry_date = card_expiry.split('/')
        if len(expiry_date) != 2:
            messagebox.showwarning("Invalid Information!", "Invalid expiration date! Please enter a valid expiration date.")
            return
        
        expiry_month = expiry_date[0]
        expiry_year = "20" + expiry_date[1]
        today = datetime.today()
        
        if int(expiry_month) < 1 or int(expiry_month) > 12:
            messagebox.showwarning("Invalid Information!", "Invalid expiration date! Please enter a valid expiration date.")
            return
        
        if int(expiry_year) < today.year or (int(expiry_year) == today.year and int(expiry_month) < today.month):
            messagebox.showwarning("Invalid Information!", "Card has expired.")
            return
        
        # Card CVV validation
        if len(card_cvv) != 3:
            messagebox.showwarning("Invalid Information!", "Invalid CVV! Please enter a valid CVV.")
            return
        
        # Create order object
        est_time = today + timedelta(minutes=30)
        self.order = {
            "order_num": random.randint(000000,999999),
            "order_item": self.cart,
            "datetime":  est_time.strftime('%m-%d-%Y %H:%M:%S')
        }
        self.orders.append(self.order)
        
        # Display success message and navigate to order page
        messagebox.showinfo("Placed order successfully", "Thank you for your order! Your pizza will be delivered soon.")
        self.cart = []
        self.orderPage()
    
    def orderPage(self):
        '''
        Create the Order page
        Parameters:
            None
        Returns:
            None
        '''
        self.clear_frame(self.body)
        
        # If has orders -> display orders
        # Else -> display empty messages
        if self.orders:
            for order in self.orders:
                item_frame = tk.Frame(self.body)
                item_frame.pack(fill=tk.X, padx=5, pady=5)
                tk.Label(item_frame, text=f"Order #{order['order_num']} - Status: Out for delivery.", font='Helvetica 15').pack(padx=300)
                tk.Label(item_frame, text=f"Estimated delivery by {order['datetime']}", font='Helvetica 10').pack(anchor=tk.W, padx=300)
        else:
            item_frame = tk.Frame(self.body)
            item_frame.pack(fill=tk.X, padx=5, pady=5)
            tk.Label(item_frame, text="You have no orders placed yet.", font='Helvetica 15').pack(padx=300)
        
    def scrollableCanvas(self):
        '''
        Create a scrollable canvas
        Parameters:
            None
        Returns:
            canvas (Canvas): the Canvas
            scrollable_frame (Frame): the scrollable frame
        '''
        canvas = tk.Canvas(self.root)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        return canvas, scrollable_frame
            
    def clear_frame(self, frame):
        '''
        Clear all widgets in the given frame
        Parameters:
            frame (tk.Frame): the frame to clear
        Returns:
            None
        '''
        if frame:
            for widget in frame.winfo_children():
                widget.destroy()

# Run the application
app = PalacePizza()