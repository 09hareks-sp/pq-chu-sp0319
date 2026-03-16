## Main file for user interface
import tkinter as tk
from tkinter import N, W, E, S
from tkinter import ttk

class PQApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
    
        self.l_a:tk.StringVar = tk.StringVar()
        self.l_b:tk.StringVar = tk.StringVar()
        self.l_c:tk.StringVar = tk.StringVar()
        self.r_a:tk.StringVar = tk.StringVar()
        self.r_b:tk.StringVar = tk.StringVar()
        self.r_c:tk.StringVar = tk.StringVar()
        
        self.init_widgets()
        self.grid()

    def init_widgets(self):
        mainframe = ttk.Frame(self, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.left_a_entry = tk.Entry(mainframe, width=5, textvariable=self.l_a)
        self.left_a_entry.grid(column=0,row=1)
        self.left_a_label = ttk.Label(mainframe, text="x^2 +").grid(column=1,row=1)

        self.left_b_entry = tk.Entry(mainframe, width=5, textvariable=self.l_b)
        self.left_b_entry.grid(column=2,row=1)
        self.left_b_label = ttk.Label(mainframe, text="x +").grid(column=3,row=1)

        self.left_c_entry = tk.Entry(mainframe, width=5, textvariable=self.l_c)
        self.left_c_entry.grid(column=4,row=1)
        self.left_c_label = ttk.Label(mainframe, text=" = ").grid(column=5,row=1)

        self.right_a_entry = tk.Entry(mainframe, width=5, textvariable=self.r_a)
        self.right_a_entry.grid(column=6,row=1)
        self.right_a_label = ttk.Label(mainframe, text="x^2 +").grid(column=7,row=1)

        self.right_b_entry = tk.Entry(mainframe, width=5, textvariable=self.r_b)
        self.right_b_entry.grid(column=8,row=1)
        self.right_b_label = ttk.Label(mainframe, text="x +").grid(column=9,row=1)

        self.right_c_entry = tk.Entry(mainframe, width=5, textvariable=self.r_c)
        self.right_c_entry.grid(column=10,row=1)

        self.quit_button = tk.Button(self, text='Exit', command=self.quit)
        self.quit_button.grid(column=0, row=2, sticky=(W,S))

        self.solve_button = tk.Button(self, text='Solve', command=self.solve)
        self.solve_button.grid(column=1, row=2 )

    def solve(self):
        print("The solve button was pressed")
        #self.read_fields()
        print(self.l_a.get(), " - ",self.l_b.get() , " - ",self.l_c.get() , " - ",self.r_a.get(), " - ",self.r_b.get(), " - ",self.r_c.get())

    def read_fields(self):
        self.l_a=self.left_a_entry.get()
        self.l_b=self.left_b_entry.get()
        self.l_c=self.left_c_entry.get()        
        self.r_a=self.right_a_entry.get()        
        self.r_b=self.right_b_entry.get()        
        self.r_c=self.right_c_entry.get()


app = PQApp()
app.master.title('PQ-chu')
app.mainloop()