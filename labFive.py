import tkinter as tk
import subprocess as sp
#from time import sleep

window = tk.Tk()
i = 0
label_text = tk.StringVar(window)
label_text.set("Hello, Tkinter " + str(i))

def add_one():
    global i
    i = i+1
    return i

def windows_calculator():
    sp.Popen(r"C:\Program Files\WindowsApps\Microsoft.WindowsCalculator_11.2307.4.0_x64__8wekyb3d8bbwe\CalculatorApp.exe")
    return

def update():
    add_one()
    global label_text
    label_text.set("Hello, Tkinter " + str(i))
    #greeting["text"] = label_text.get()
    global entry
    #entry.insert(0, label_text.get())
    return

window_size = "854x480"
window.geometry(window_size)

window.title("Title")

#window.grid(int(854/16),int(480/9),16,9)

frame_one = tk.Frame(window, relief=tk.FLAT)
frame_two = tk.Frame(window, relief=tk.RAISED)
frame_three = tk.Frame(window, relief=tk.SUNKEN)
greeting = tk.Label(master=frame_one, text="", textvariable=label_text, bg="yellow")
entry = tk.Entry(master=frame_one, textvariable=label_text, bg="light blue")
button_one = tk.Button(master=frame_one, text="Press", borderwidth=1, command=update, bg="light blue")
button_calculator = tk.Button(master=frame_two, text="Calculator", borderwidth=1, command=windows_calculator, bg="green")
text_widget = tk.Text(master=frame_three)

#text_widget.insert(1, "text box")
#entry.insert(label_text)
#greeting.place(x=10,y=10)
#button_one.place(x=10,y=20)

frame_one.pack()
frame_two.pack()
frame_three.pack()
greeting.pack()
entry.pack()
button_one.pack()
button_calculator.pack()
text_widget.pack()

tk.mainloop()
