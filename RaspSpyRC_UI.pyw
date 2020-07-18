import tkinter as tk
import RaspSpyRC_Movement as RSRC
import time


root = tk.Tk()
root.title('RaspSpy RC')
#Sets up main window
frame = tk.Frame(root, width=800, height=600, bg='#FFFFFF')
frame.pack(fill='x')
Directions=[]
secInput = tk.Text(frame, width=29, height=1)
directionLabel = tk.Label(frame, text='Previous Movments Shows Here', bg='white', fg='black', width=90, height=3)
directionLabel.grid(row = 0, columnspan = 9)

#StoreInput Script
def storeInput():
    directionLabel.config(text='')
    directionLabel.config(text=Directions)
#Hover Buttons
def forwardHover(e):
    buttonLabel.config(text='This Causes The Robot To Move Forward For Set Amount Of Seconds')
def stopHover(e):
    buttonLabel.config(text='This Will Stop All Scripts Closing This Application')
def leftHover(e):
    buttonLabel.config(text='This Will Cause The Robot To Turn Left For Set Amount Of Time')
def waitHover(e):
    buttonLabel.config(text='This Pauses The Program For A Set Amount Of Time')
def rightHover(e):
    buttonLabel.config(text='This Will Cause The Robot To Turn Right For Set Amount Of Time')
def resetHover(e):
    buttonLabel.config(text='Enter Your Time Of Movement In The Text Box Above Then Click What Direction You Want, All Movement Will Be Stored On Log.txt')
#Forward Script
def forward():
    number=secInput.get('1.0', 'end-1c')
    if (number == ''):
        number='1'
    RSRC.Forward(number)
    secInput.delete('1.0', 'end')
    Directions.append('Forward ' + number)
    storeInput()
#Left Script
def left():
    number=secInput.get('1.0', 'end-1c')
    if (number == ''):
        number='1'
    RSRC.Left(number)
    secInput.delete('1.0', 'end')
    Directions.append('Left ' + number)
    storeInput()
#Right Script
def right():
    number=secInput.get('1.0', 'end-1c')
    if (number == ''):
        number='1'
    RSRC.Right(number)
    secInput.delete('1.0', 'end')
    Directions.append('Right ' + number)
    storeInput()
#Wait Script
def wait():
    number=secInput.get('1.0', 'end-1c')
    if (number == ''):
        number='1'
    RSRC.Wait(number)
    secInput.delete('1.0', 'end')
    Directions.append('Wait ' + number)
    storeInput()
#Shutdown Script
def shutdown():
    number=secInput.get('1.0', 'end-1c')
    if (number == ''):
        number='1'
    secInput.delete('1.0', 'end')
    RSRC.Stop(number)
    exit()
#Popup Script
def stop():
    popup = tk.Tk()
    popup.title('RaspSpy RC Popup')
    
    w = 400
    h = 200
    sw = popup.winfo_screenwidth()
    sh = popup.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    m = 'Thank You For Using RaspSpy RC'
    m += '\n'
    w = tk.Label(popup, text=m, width=50, height=10)
    w.pack()
    b = tk.Button(popup, text="Close Port And Shutdown", command=lambda: [popup.destroy(),shutdown()], width=20)
    b.pack()
    popup.mainloop()

    
#Makes Buttons
Forward = tk.Button(frame, text='Forward', width=6, height=3, fg='#110c15', bg='#FFFFFF', command=forward)
Forward.grid(row = 6, column = 44)
Stop = tk.Button(frame, text='Stop', width=6, height=3, fg='#110c15', bg='#FFFFFF', command=stop)
Stop.grid(row = 6, column = 45)
Left = tk.Button(frame, text='Left', width=6, height=3, fg='#110c15', bg='#FFFFFF', command=left)
Left.grid(row = 7, column = 43)
Right = tk.Button(frame, text='Right', width=6, height=3, fg='#110c15', bg='#FFFFFF', command=right)
Right.grid(row = 7, column = 45)
Wait = tk.Button(frame, text='Wait', width=6, height=3, fg='#110c15', bg='#FFFFFF', command=wait)
Wait.grid(row = 7, column = 44)
#Makes Labels
secLabel = tk.Label(frame, text='Input Running Seconds, Then Click Direction Of Travel, !MUST ENTER A NUMBER, If No Entry Default 1!', bg='#FFFFFF')
secLabel.grid(row = 8, columnspan = 3, stick='W')
secInput = tk.Text(frame, width=29, height=1)
secInput.grid(row = 8, columnspan = 46, stick='E')
buttonLabel = tk.Label(frame, text='Enter Your Time Of Movement In The Text Box Above Then Click What Direction You Want, All Movement Will Be Stored On Log.txt', bd=1, relief='sunken', anchor='e', width=120, bg='#FFFFFF')
buttonLabel.grid(row = 10, columnspan = 46)

#Makes Button Description
Forward.bind("<Enter>", forwardHover)
Stop.bind("<Enter>", stopHover)
Left.bind("<Enter>", leftHover)
Wait.bind("<Enter>", waitHover)
Right.bind("<Enter>", rightHover)
Forward.bind("<Leave>", resetHover)
Stop.bind("<Leave>", resetHover)
Left.bind("<Leave>", resetHover)
Wait.bind("<Leave>", resetHover)
Right.bind("<Leave>", resetHover)


root.mainloop()

