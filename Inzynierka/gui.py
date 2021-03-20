import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import tkinter as tk
from matplotlib import style

style.use('ggplot')
# from tkinter import ttk ulepszenie guzikow (zamiana tk na ttk)

import methods

LARGE_FONT = ("Courier", 30)
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pullData = open('przemieszczenie.txt', 'r').read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    a.clear()
    a.plot(xar, yar)

class powerApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Power app")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, FirstPage, SecondPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameU = tk.Frame()
        frameL = tk.Frame()
        frameR = tk.Frame()
        title = tk.Label(master = frameU, text="Aplikacja do pomiaru mocy podczas przysiadu ze sztangą", borderwidth=2, relief="groove")
        title.config(font=("Courier", 30))
        title.pack()

        label = tk.Label(master=frameL, text="Wprowadz mase człowieka [kg]: ")
        label.grid(column=0, row=0)
        label1 = tk.Label(master=frameL, text="Wprowadz mase obciazenia [kg]: ")
        label1.grid(column=0, row=1)
        label2 = tk.Label(master=frameL, text="Wprowadz wzrost ćwiczącego [cm]: ")
        label2.grid(column=0, row=2)

        frameL.txtEntry = methods.Prox(frameL, width=10)
        frameL.txtEntry1 = methods.Prox(frameL, width=10)
        frameL.txtEntry2 = methods.Prox(frameL, width=10)
        frameL.txtEntry.grid(column=1, row=2)
        frameL.txtEntry1.grid(column=1, row=3)
        frameL.txtEntry2.grid(column=1, row=4)
        btn = tk.Button(master=frameL, text="Zacznij pomiary", command=lambda: methods.clicked(self.txtEntry, self.txtEntry1, self.txtEntry2))
        btn.grid(column=0, row=5)
        btn1 = tk.Button(frameL, text="Koniec pomiarów", command=lambda: methods.end())
        btn1.grid(column=1, row=5)

        frameL.pack()

class FirstPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wprowadz mase człowieka [kg]: ")
        label.grid(column=0, row=0)
        label1 = tk.Label(self, text="Wprowadz mase obciazenia [kg]: ")
        label1.grid(column=0, row=1)
        label2 = tk.Label(self, text="Wprowadz wzrost ćwiczącego [cm]: ")
        label2.grid(column=0, row=2)

        self.txtEntry = methods.Prox(self, width=10)
        self.txtEntry1 = methods.Prox(self, width=10)
        self.txtEntry2 = methods.Prox(self, width=10)
        self.txtEntry.grid(column=1, row=0)
        self.txtEntry1.grid(column=1, row=1)
        self.txtEntry2.grid(column=1, row=2)
        btn = tk.Button(self, text="Zacznij pomiary", command=lambda: methods.clicked(self.txtEntry, self.txtEntry1, self.txtEntry2))
        btn.grid(column=0, row=3)
        btn1 = tk.Button(self, text="Wróć do strony startowej", command=lambda: controller.show_frame(StartPage))
        btn1.grid(column=1, row=3)
        btn2 = tk.Button(self, text="Koniec pomiarów", command=lambda :methods.end())
        btn2.grid(column=1, row=4)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()


        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = powerApp()
ani = animation.FuncAnimation(f, animate, interval=100)
app.mainloop()
