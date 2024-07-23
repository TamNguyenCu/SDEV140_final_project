import tkinter as tk
from tkinter import messagebox
import json

cart = []
  
class App(tk.Tk):
    def __init__(self, *args, **kwargs): 
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Pizza Palace")
        self.geometry("800x600")
        self.maxsize(800, 600)
        
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}  
        for F in (Main, Menu, Order):
  
            frame = F(container, self)
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(Main)        
        self.mainloop()
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class Main(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        main_frame_bg = tk.Label(
            self, bg="#009246")
        main_frame_bg.place(relheight=1, relwidth=1)
        
        welcome_label = tk.Label(
            self, 
            text="Welcome to Palace Pizza!", 
            fg="#ffffff", 
            bg="#009246",
            font=('Helvetica 20 bold italic')
        )
        welcome_label.place(relx=0.5, rely=0.3, anchor="center")
        
        start_ord_btn = tk.Button(
            self,
            text="Start your orders here!",
            width=19,
            height=3,
            font=('Helvetica 15 bold'),
            command = lambda : controller.show_frame(Menu)
        )
        start_ord_btn.place(relx=0.5, rely=0.5, anchor="center")
  
class Menu(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        homeBtn = tk.Button(self, text="Pizza Palace", bd=0, font='Helvetica 20 bold italic',
                               command = lambda : controller.show_frame(Main))
        homeBtn.grid(row=0, column=0, ipadx=50, pady=10)
        
        menuNavBtn = tk.Button(self, text="Menu", bd=0, font='Helvetica 18 bold',
                               command = lambda : controller.show_frame(Menu))
        menuNavBtn.grid(row=0, column=1, padx=70, pady=10)
        
        orderNavBtn = tk.Button(self, text="Orders", bd=0, font='Helvetica 18 bold',
                                command = lambda : controller.show_frame(Order))
        orderNavBtn.grid(row=0, column=2, padx=70, pady=10)
        
        self.item_frame = tk.Frame(self)
        self.item_frame.grid(row=1, column=1, columnspan=5, rowspan= 5)
        
        pizzaBtn = tk.Button(self, text="Pizza", bd=0, font='Helvetica 15 bold', command=self.pizzaItems)
        pizzaBtn.grid(row=1, column=0, pady=10)
        
        sidesBtn = tk.Button(self, text="Sides", bd=0, font='Helvetica 15 bold', command=self.sideItems)
        sidesBtn.grid(row=2, column=0, pady=10)
        
        drinksBtn = tk.Button(self, text="Drinks", bd=0, font='Helvetica 15 bold', command=self.drinkItems)
        drinksBtn.grid(row=3, column=0, pady=10)
        
        file = open('data.json')
        data = json.load(file)
        self.pizzas = data['pizzas']
        self.sides = data['sides']
        self.drinks = data['drinks']
        file.close()
        self.pizzaItems()
    
    def pizzaItems(self):
        self.clear_frame()
        c = 0
        r = 0
        for pizza in self.pizzas:
            if c > 2:
                r += 1
                c = 0
            itemLable = tk.Button(self.item_frame, text=f"{pizza['name']}\n{pizza['price']}", bd=0, font='Helvetica')
            itemLable.grid(column=c, row=r, padx=5, pady=5)
            c += 1
        
    
    def sideItems(self):
        self.clear_frame()
        c = 0
        r = 0
        for side in self.sides:
            if c > 2:
                r += 1
                c = 0
            itemLable = tk.Button(self.item_frame, text=f"{side['name']}\n{side['price']}", bd=0, font='Helvetica')
            itemLable.grid(column=c, row=r, padx=5, pady=5)
            c += 1
    
    def drinkItems(self):
        self.clear_frame()
        c = 0
        r = 0
        for drink in self.drinks:
            if c > 2:
                r += 1
                c = 0
            itemLable = tk.Button(self.item_frame, text=f"{drink['name']}\n{drink['price']}", bd=0, font='Helvetica')
            itemLable.grid(column=c, row=r, padx=5, pady=5)
            c += 1
    
    def clear_frame(self):
        for widget in self.item_frame.winfo_children():
            widget.destroy()
        
class Order(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        homeBtn = tk.Button(self, text="Pizza Palace", bd=0, font='Helvetica 20 bold italic',
                               command = lambda : controller.show_frame(Main))
        homeBtn.grid(row=0, column=0, ipadx=50, pady=10)
        
        menuNavBtn = tk.Button(self, text="Menu", bd=0, font='Helvetica 18 bold',
                               command = lambda : controller.show_frame(Menu))
        menuNavBtn.grid(row=0, column=2, ipadx=70, pady=10)
        
        orderNavBtn = tk.Button(self, text="Orders", bd=0, font='Helvetica 18 bold',
                                command = lambda : controller.show_frame(Order))
        orderNavBtn.grid(row=0, column=4, ipadx=70, pady=10)

    def orderItems(self):
        if len(cart) == 0:
            messagebox.showinfo("Oops!", " Look like you have not place any order yet")

app = App()