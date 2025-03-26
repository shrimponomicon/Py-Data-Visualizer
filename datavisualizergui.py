'''
Derrian Cooper
March 20,2025
data visualizer
'''
import tkinter as tk
import tkinter.messagebox #for button responses
import turtle as t

GRAPH_SCALE = 20
t.setup(500,250)
t.title('Visualizer')



def main():
    graph_gui=GraphTemplate()

class GraphTemplate:
    def __init__(self):

        #main window
        self.mainWindow = tk.Tk()#always include 'self' because self is the object being passed.
        self.mainWindow.title('Graph Config')


        

        #self.quitButton=tk.Button(self.bottomFrame,
         #                              text='Exit',
        #                               command=self.mainWindow.destroy)
        #self.quitButton.pack(side='left')


        #graph window

        self.topFrame = tk.Frame()
        self.midFrame = tk.Frame()
        self.bottomFrame = tk.Frame()

        #events
        self.isValid = tk.StringVar()
        self.validationLabel = tk.Label(self.topFrame,
                                        textvariable=self.isValid)
        self.validationLabel.pack(side='left')
        self.startButton=tk.Button(self.bottomFrame,
                                        text='Start Program',
                                        command=self.initializeGraph)
        self.startButton.pack(side='left')
        self.clearButton=tk.Button(self.bottomFrame,
                                        text='Clear Program',
                                        command=self.clearTurtle)
        self.clearButton.pack(side='left')

        

        


        
        

        self.topFrame.pack()
        self.midFrame.pack()
        self.bottomFrame.pack()

        tk.mainloop()
        

    def initializeGraph(self):
        self.inputLabel= tk.Label(self.mainWindow,text="Give a value for X1")
        self.inputLabel.pack(side='left')
        self.x1Entry=tk.Entry(self.mainWindow,
                              width=5)
        self.x1Entry.pack()
        
        self.inputLabel= tk.Label(self.mainWindow,text="Give a value for X2")
        self.inputLabel.pack(side='left')
        self.x2Entry=tk.Entry(self.mainWindow,
                              width=5)
        self.x2Entry.pack()
        
        self.inputLabel= tk.Label(self.mainWindow,text="Give a value for Y1")
        self.inputLabel.pack(side='left')
        self.y1Entry=tk.Entry(self.mainWindow,
                              width=5)
        self.y1Entry.pack()
        
        self.inputLabel= tk.Label(self.mainWindow,text="Give a value for Y2")
        self.inputLabel.pack(side='left')
        self.y2Entry=tk.Entry(self.mainWindow,
                              width=5)
        self.y2Entry.pack()

        
        t.hideturtle()
        t.penup()
        t.goto(-500,-125)

        #use radios to info boxes
        x_coord = list(range(1,10,2))#1,3,5,7,9
        y_coord = list(range(0,5,1))#0,1,2,3,4
        for val in y_coord:
            print(f"{y_coord[val]},{x_coord[val]}")

        graph_domain = t.numinput("Input Needed", "Enter the domain of your data")
        graph_range = t.numinput("Input Needed", "Enter the range of your data")
        
        if graph_domain == 1 and graph_range == 1:
            validation="Working."
            self.isValid.set(validation)
            for val in y_coord:
                one_x= x_coord[val]
                one_y= y_coord[val]

                #should change from goto to forward and set rotation methods
                t.goto((one_x *GRAPH_SCALE), (one_y *GRAPH_SCALE)) #maintains ratio while making data more visible
                t.write(f"{one_y},{one_x}") #backwards because domain and range are swapped in turtle graph
                t.dot()
            #t.write(f"{y_coord[-1]},{x_coord[-1]}")
        else:
            validation="Error: Bad Domain"
            self.isValid.set(validation)
            t.bgcolor('dark salmon') #salmon bad
            
            tkinter.messagebox.showinfo("Error",validation)
            t.clearscreen()
            self.isValid.set(" ")
            
            
        
            
    def clearTurtle(self):
        t.clearscreen()
        self.isValid.set(" ")
        

if __name__=='__main__':
    main()
