import threading
from tkinter import *
from tkinter import ttk

import tk
import matplotlib.pyplot as plt

from matplotlib import style, animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk as NavigationToolbar2TkAgg

import methods

style.use('ggplot')
f = Figure(figsize=(12, 8), dpi=100)
#f = plt.figure()
a = f.add_subplot(311)
b = f.add_subplot(312)
c1 = f.add_subplot(313)

def animate(i):
    pullData = open('przemieszczenie.txt', 'r').read()
    pullData1 = open('predkosc.txt', 'r').read()
    pullData2=open('przyspieszenie.txt', 'r').read()
    dataArray = pullData.split('\n')
    dataArray1 = pullData1.split('\n')
    dataArray2 = pullData2.split('\n')
    xar = []
    yar = []
    xbr = []
    ybr = []
    xcr = []
    ycr = []
    for eachLine in dataArray:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
    for eachLine in dataArray1:
        if len(eachLine) > 1:
            x1, y1 = eachLine.split(',')
            xbr.append(float(x1))
            ybr.append(float(y1))
    for eachLine in dataArray2:
        if len(eachLine) > 1:
            x2, y2 = eachLine.split(',')
            xcr.append(float(x2))
            ycr.append(float(y2))
    a.clear()
    a.plot(xar, yar)
    b.clear()
    b.plot(xbr, ybr)
    c1.clear()
    c1.plot(xcr, ycr)
    return a,b,c1



class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Aplikacja do pomiaru mocy")

        #for r in range(1):
        #    self.master.rowconfigure(r,minsize=300 ,weight=1)
        #for c in range(6):
        #    self.master.columnconfigure(c,minsize=400,weight=1)



        #frame1 = Frame(master)
        frame1 = LabelFrame(master, text='Dane ćwiczącego', width = 1500, height = 130, bd=5)
        frame1.grid(row=0, column=0, sticky=W + E + N + S)
        #frame1.pack(side=LEFT)
        label = ttk.Label(master=frame1, text="Wprowadz mase człowieka [kg]: ")
        label.grid(column=0, row=0, sticky=W)
        #label.pack(side=TOP, pady = 3)
        label1 = ttk.Label(master=frame1, text="Wprowadz mase obciazenia [kg]: ")
        label1.grid(column=0, row=1, sticky=W)
        #label1.pack(side=LEFT, pady = 6)
        label2 = ttk.Label(master=frame1, text="Wprowadz wzrost ćwiczącego [cm]: ")
        label2.grid(column=0, row=2, sticky=W)
        #label2.pack(side=LEFT)
        frame1.txtEntry = methods.Prox(frame1, width=15)
        frame1.txtEntry1 = methods.Prox(frame1, width=15)
        frame1.txtEntry2 = methods.Prox(frame1, width=15)
        frame1.txtEntry.grid(column=1, row=0)
        frame1.txtEntry1.grid(column=1, row=1)
        frame1.txtEntry2.grid(column=1, row=2)
        #frame1.txtEntry.pack(side=RIGHT)
        #frame1.txtEntry1.pack(side=RIGHT)
        #frame1.txtEntry2.pack(side=RIGHT)
        btn = ttk.Button(master=frame1, text="Zacznij pomiary",command=lambda: methods.clicked(frame1.txtEntry, frame1.txtEntry1, frame1.txtEntry2))
        btn.grid(column=0, row=5, sticky=W)
        #btn.pack(side=BOTTOM)
        btn1 = ttk.Button(frame1, text="Koniec pomiarów", command=lambda: methods.stop())
        btn1.grid(column=0, row=5, sticky=E)
        #btn1.pack(side=BOTTOM)
#--------------------------------PRAWA STRONA---------------------------------------------------------------------------------------------------------#
        frame2 = Frame(master)
        #frame2 = LabelFrame(master, text="Wykresy", width=1500, height=500, bd=5)
        frame2.grid(row=0, column=1, sticky = W+E+N+S)
        #frame2.pack(side=RIGHT)
        #tabControl = ttk.Notebook(frame2)

        #tab1 = ttk.Frame(tabControl)
        #tab2 = ttk.Frame(tabControl)
        #tab3 = ttk.Frame(tabControl)
        #tab4 = ttk.Frame(tabControl)

        ##tabControl.add(tab1, text='Wykresy')
        #tabControl.add(tab2, text='Wyniki')
        #tabControl.add(tab3, text='Predkosc')
        #tabControl.add(tab4, text='Przyspieszenie')
        #methods.chart('przemieszczenie.txt', f)
        ##methods.chart('predkosc.txt', f)
        #methods.chart('przyspieszenie.txt', f)

        f.text(0.5, 0.04, 'Time [s]', ha='center', va='center')
        f.text(0.07, 0.23, 'Acceleration [m/s^2]', ha='center', va='center', rotation='vertical')
        f.text(0.07, 0.5, 'Velocity [m/s]', ha='center', va='center', rotation='vertical')
        f.text(0.07, 0.77, 'Displacement [m]', ha='center', va='center', rotation='vertical')
        canvas = FigureCanvasTkAgg(f, frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        toolbar = NavigationToolbar2TkAgg(canvas, frame2)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

root = Tk()
root.geometry("1500x850")
root.resizable(False, False)
app = Application(master=root)
ani1 = animation.FuncAnimation(f, animate, interval=1)




app.mainloop()
