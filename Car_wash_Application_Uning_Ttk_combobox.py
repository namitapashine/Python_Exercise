from tkinter import *
from tkinter import ttk
from tkinter import messagebox

main_window = Tk()
main_window.title("Welcome to Namita's Car Wash")
main_window.geometry("300x200")
# Maximize the window (works on Windows)
main_window.state('zoomed')

# Frame 1: -------------------------------------
frame1 = Frame(main_window, bg="lightblue", bd=20)  # Create the frame with a background color
frame1.pack(fill="both")  # Add the frame to the main window and fill both

label1 = Label(frame1, text="Welcome to Namita's Car Wash Services", font="bold",bg="lightblue", bd=0)
label1.pack()

# Frame 2 : ------------------------------------
frame2 = Frame(main_window, bg="lightgreen", bd=100)  # Create the frame with a background color
frame2.pack(side=LEFT, fill="both")  # Add the frame to the main window and fill both

label2 = Label(frame2, text="Select a service",bg="lightgreen")
label2.pack()
#label2.place(x=2,y=2,width=140)

# Dictionary for services and their prices
avlbl_services = {
    "Basic Wash": "20$",
    "Deluxe Wash": "30$",
    "Premium Wash": "40$"
}

# Dropdown (Combobox) for car wash services
choice_combobox = ttk.Combobox(frame2, values=list(avlbl_services.keys()), state="readonly")
choice_combobox.pack(pady=2)

# Variable to hold the message widget
msg = None

def msgdisplay():
    global msg  # Declare msg as a global variable
    # If a message already exists, destroy it
    if msg is not None:
        msg.destroy()
    # Create a new message and pack ite
    
    msg = Message(frame3, text="Ok Thank You, We will do the needful. Don't forget to take your token.", width=400, bg="lightyellow")
    msg.pack()

but1=ttk.Button(frame2,text="OK",command= msgdisplay)
but1.pack(pady=30)


# Class for option selection
class OptionSelection:
    def __init__(self):
        pass

    def choose(self, event):  # Event parameter to bind the combobox selection
        element = choice_combobox.get()  # Get the selected service
        if element == "Basic Wash":
            service = avlbl_services["Basic Wash"]
            messagebox.showinfo("Service Info", f"The Price for Basic Wash is {service}")
        elif element == "Deluxe Wash":
            service = avlbl_services["Deluxe Wash"]
            messagebox.showinfo("Service Info", f"The Price for Deluxe Wash is {service}")
        elif element == "Premium Wash":
            service = avlbl_services["Premium Wash"]
            messagebox.showinfo("Service Info", f"The Price for Premium Wash is {service}")

# Create an object of the OptionSelection class
obj = OptionSelection()

# Bind the combobox selection to the choose method
choice_combobox.bind("<<ComboboxSelected>>", obj.choose)


# Frame 3 : ---------------------------------------
frame3 = Frame(main_window, bg="lightyellow", bd=100)  # Create the frame with a background color
frame3.pack(fill="both")  # Add the frame to the main window and fill both



main_window.mainloop()