import tkinter as tk

cart = []
  
class mainApp(tk.Tk):
     
    # __init__ function
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
        for F in (menuPage, orderPage):
  
            frame = F(container, self)
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.title("Pizza Palace")
        self.show_frame(menuPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
class menuPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width=800, height=600)
        canvas.grid(columnspan=12, rowspan=12)
        
        homeLabel = tk.Label(self, text="Pizza Palace", font='helvetica, 20')
        homeLabel.grid(columnspan=4, column=0, row=0)
        
        menuNavBtn = tk.Button(self, text="Menu", bd=0, font='helvetica',
                               command = lambda : controller.show_frame(menuPage))
        menuNavBtn.grid(columnspan=4, column=4, row=0)
        
        orderNavBtn = tk.Button(self, text="Orders", bd=0, font='helvetica',
                                command = lambda : controller.show_frame(orderPage))
        orderNavBtn.grid(columnspan=4, column=8, row=0)
        
        pizzaCatBtn = tk.Button(self, text="Pizza", bd=0, font='helvetica', command=self.pizzaItems)
        pizzaCatBtn.grid(columnspan=3, column=0, row=2)
        
        sideCatBtn = tk.Button(self, text="Sides", bd=0, font='helvetica', command=self.sideItems)
        sideCatBtn.grid(columnspan=3, column=0, row=3)
        
        drinkCatBtn = tk.Button(self, text="Drinks", bd=0, font='helvetica', command=self.drinkItems)
        drinkCatBtn.grid(columnspan=3, column=0, row=4)
    
    def pizzaItems(self):
        emptyLable = tk.Label(self, text="Pizza items go here", font='helvetica')
        emptyLable.grid(column=6, row=3, sticky ="nsew")
    
    def sideItems(self):
        emptyLable = tk.Label(self, text="Side items go here", font='helvetica')
        emptyLable.grid(column=6, row=3, sticky ="nsew")
    
    def drinkItems(self):
        emptyLable = tk.Label(self, text="Drink items go here", font='helvetica')
        emptyLable.grid(column=6, row=3, sticky ="nsew")

class orderPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, width=800, height=600)
        canvas.grid(columnspan=12, rowspan=12)
        
        homeLabel = tk.Label(self, text="Pizza Palace", font='helvetica, 20')
        homeLabel.grid(columnspan=4, column=0, row=0)
        
        menuNavBtn = tk.Button(self, text="Menu", bd=0, font='helvetica',
                               command = lambda : controller.show_frame(menuPage))
        menuNavBtn.grid(columnspan=4, column=4, row=0)
        
        orderNavBtn = tk.Button(self, text="Orders", bd=0, font='helvetica',
                                command = lambda : controller.show_frame(orderPage))
        orderNavBtn.grid(columnspan=4, column=8, row=0)
        
        self.orderItems()

    def orderItems(self):
        if len(cart) == 0:
            emptyLable = tk.Label(self, text="Oops! Look like you haven't place any order yet", font='helvetica')
            emptyLable.grid(columnspan=6, column=3, row=6)
app = mainApp()
app.mainloop()