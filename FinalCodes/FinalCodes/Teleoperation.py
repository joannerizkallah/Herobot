#Teleoperation using CustomTkinter
#Teleoperation features a login system, mode selection, and manual mode menu (3 frames total)
import customtkinter
import tkinter
from Navigate import *
from MazeSolver import *
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue") # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
rover = Navigate()
rover.init()
maze = MazeSolver()
maze.init()
app.geometry("500x340")
def manual():
    app2 = customtkinter.CTk() 
    app2.geometry("400x240")
    
    button_up = customtkinter.CTkButton(master=app2, text="↑", command = lambda: forward())
    button_up.place(relx =0.5, rely =0.2, anchor = tkinter.CENTER)
    button_up.bind("<ButtonRelease>", on_release)
    
    button_down = customtkinter.CTkButton(master=app2, text="↓", command=lambda: reverse())
    button_down.place(relx =0.5, rely =0.8, anchor = tkinter.CENTER)
    button_down.bind("<ButtonRelease>", on_release)
    
    button_right = customtkinter.CTkButton(master=app2, text="→", command=lambda: right())
    button_right.place(relx =0.8, rely =0.5, anchor = tkinter.CENTER)
    button_right.bind("<ButtonRelease>", on_release)
    
    button_left = customtkinter.CTkButton(master=app2, text="←", command=lambda: left())
    button_left.place(relx =0.2, rely =0.5, anchor = tkinter.CENTER)
    button_left.bind("<ButtonRelease>", on_release)
    
    label = customtkinter.CTkLabel(master=app2,
                               text="Speed (HIGH -> LOW",
                               width=120,
                               height=20,
                               corner_radius=8)
    label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    slider = customtkinter.CTkSlider(master=app2,
                                 width=100,
                                 height=16,
                                 border_width=5.5, command = slider_event)
    slider.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    app2.mainloop()
    
def forward():
        rover.setPWM(100)
        rover.run('forward')
        
def slider_event(value):
        rover.setPWM(value*100)
        print("PWM: " + str(value*100))
        
def on_release(event):
        rover.run('stop')
        print('release')
        
def reverse():
        rover.setPWM(100)
        rover.run('reverse')
        
def left():
        rover.setPWM(100)
        rover.run('left')

def right():
        rover.setPWM(100)
        rover.run('right')
    
    
def button_function(): #used for debugging
    print("button pressed")

def solve_maze():
    maze.solve()


def welcome():
    app1 = customtkinter.CTk()
    app1.geometry("400x240")
    button_manual = customtkinter.CTkButton(master=app1, text="Manual Mode", command=manual)
    button_manual.place(relx =0.2, rely =0.5, anchor = tkinter.CENTER)
    button_maze = customtkinter.CTkButton(master=app1, text="Maze Solver Mode", command=solve_maze)
    button_maze.place(relx =0.7, rely =0.5, anchor = tkinter.CENTER)
    app1.mainloop()
def login(username, password):
    if(username == "joanne.rizkallah" and password == "1234"):
        app.destroy()
        welcome()
    elif(username == "nadine.sfeir" and password == "1234"):
        welcome()
        app.destroy()
    elif(username == "christy.skaff" and password == "1234"):
        welcome()
        app.destroy()
    elif(username == "noel.maalouf" and password == "MCE411"):
        welcome()
        app.destroy()
    else:
        not_welcome = customtkinter.CTk()
        not_welcome.geometry("800x800")
        not_welcome_label = customtkinter.CTkLabel(master = not_welcome, text = "NOT WELCOME")
        not_welcome_label.place(relx = 0.5, rely = 0.4, anchor = tkinter.CENTER)
        app.destroy()
label = customtkinter.CTkLabel(master = app, text = "Login System")
label.place(relx = 0.5, rely = 0.4, anchor = tkinter.CENTER)

username = customtkinter.CTkEntry(master = app, placeholder_text = "Username")
username.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

password = customtkinter.CTkEntry(master = app, placeholder_text = "Password", show = "*")
password.place(relx = 0.5, rely = 0.6, anchor = tkinter.CENTER)
login_button = customtkinter.CTkButton(master = app, text = "Login", command = lambda : login(username.get(), password.get()))
login_button.place(relx = 0.5, rely = 0.7, anchor = tkinter.CENTER)
app.mainloop()