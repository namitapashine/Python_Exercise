"""
Created on Wed Sep 26 10:15:40 2024

@author: namita
"""


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")
root.geometry("800x600")  # Adjust the size for better visibility

# Frame 1: -------------------------------------
frame1 = Frame(root, bg="lightblue", bd=10, relief="groove")  # Create the frame with a background color
frame1.pack(fill="both")  # Add the frame to the main window and fill both

label1 = Label(frame1, text="Percentage Calculator", font=("Arial", 18, "bold"), bg="lightblue", bd=0)
label1.pack(pady=10)  # Added padding for better spacing

# Frame 2 : ------------------------------------
frame2 = Frame(root, bg="lightgreen", bd=10, relief="groove")  # Create the frame with a background color and border
frame2.pack(side=LEFT, fill="y", padx=20, pady=20)  # Add some padding around the frame

# Add a title label for Frame 2
label2 = Label(frame2, text="Select a Grade to Calculate the Percentage", font=("Arial", 14, "bold"), bg="lightgreen")
label2.pack(pady=10)  # Add vertical padding for better spacing

# Create a variable to store the selected option
selected_option = StringVar()

# Create Radiobuttons with better layout
radio_button1 = ttk.Radiobutton(frame2, text="Grade 1", value="1", variable=selected_option)
radio_button2 = ttk.Radiobutton(frame2, text="Grade 2", value="2", variable=selected_option)
radio_button3 = ttk.Radiobutton(frame2, text="Grade 3", value="3", variable=selected_option)

# Create a frame inside frame2 for organizing radio buttons with padding and spacing
radio_frame = Frame(frame2, bg="lightgreen")
radio_frame.pack(pady=20)

# Pack the radiobuttons with more spacing
radio_button1.pack(anchor=W, padx=10, pady=5)  # Align to the left with padding
radio_button2.pack(anchor=W, padx=10, pady=5)
radio_button3.pack(anchor=W, padx=10, pady=5)

# Add a button to trigger the check and input creation
check_button = ttk.Button(frame2, text="Calculate", command=lambda: ask_marks())
check_button.pack(pady=20)  # Add padding for spacing

# Frame 3 : ---------------------------------------
frame3 = Frame(root, bg="lightyellow", bd=10, relief="groove")  # Create the frame with a background color and border
frame3.pack(fill="both", padx=20, pady=20)  # Add the frame to the main window with padding

# Variables for input fields
input1 = None
input2 = None
input3 = None

# Function to create entry when Grade 1 is selected
def ask_marks():
    global input1, input2, input3,input4,input5
    
    if selected_option.get() == "1":  # Compare the value of selected_option
        # Clear previous input fields
        for widget in frame3.winfo_children():
            widget.destroy()
    
        
        # Create label and entry for Subject 1
        label1 = ttk.Label(frame3, text="Marks in Subject 1:")
        label1.grid(row=0, column=0, padx=10, pady=10)  # Place label in grid
        input1 = ttk.Entry(frame3)
        input1.grid(row=0, column=1, padx=10, pady=10)  # Place input box next to label

        # Create label and entry for Subject 2
        label2 = ttk.Label(frame3, text="Marks in Subject 2:")
        label2.grid(row=1, column=0, padx=10, pady=10)  # Place label in grid
        input2 = ttk.Entry(frame3)
        input2.grid(row=1, column=1, padx=10, pady=10)  # Place input box next to label

        # Create label and entry for Subject 3
        label3 = ttk.Label(frame3, text="Marks in Subject 3:")
        label3.grid(row=2, column=0, padx=10, pady=10)  # Place label in grid
        input3 = ttk.Entry(frame3)
        input3.grid(row=2, column=1, padx=10, pady=10)  # Place input box next to label

        # Create a Button to trigger the input processing
        submit_button = ttk.Button(frame3, text="Submit", command=lambda:get_marks_and_percent1())
        submit_button.grid(row=4, column=1, padx=10)
    elif selected_option.get() == "2":
        for widget in frame3.winfo_children():
            widget.destroy()
            
    
        # Create label and entry for Subject 1
        label1 = ttk.Label(frame3, text="Marks in Subject 1:")
        label1.grid(row=0, column=0, padx=10, pady=10)  # Place label in grid
        input1 = ttk.Entry(frame3)
        input1.grid(row=0, column=1, padx=10, pady=10)  # Place input box next to label

        # Create label and entry for Subject 2
        label2 = ttk.Label(frame3, text="Marks in Subject 2:")
        label2.grid(row=1, column=0, padx=10, pady=10)  # Place label in grid
        input2 = ttk.Entry(frame3)
        input2.grid(row=1, column=1, padx=10, pady=10)  # Place input box next to label

        # Create label and entry for Subject 3
        label3 = ttk.Label(frame3, text="Marks in Subject 3:")
        label3.grid(row=2, column=0, padx=10, pady=10)  # Place label in grid
        input3 = ttk.Entry(frame3)
        input3.grid(row=2, column=1, padx=10, pady=10)  # Place input box next to label

        label4 = ttk.Label(frame3, text="Marks in Subject 4:")
        label4.grid(row=3, column=0, padx=10, pady=10)  # Place label in grid
        input4 = ttk.Entry(frame3)
        input4.grid(row=3, column=1, padx=10, pady=10)  # Place input box next to label
       
        # Create a Button to trigger the input processing
        submit_button = ttk.Button(frame3, text="Submit", command=lambda:get_marks_and_percent2())
        submit_button.grid(row=4, column=1, padx=10)


    elif selected_option.get() == "3":
        for widget in frame3.winfo_children():
            widget.destroy()
            
    
        # Create label and entry for Subject 1
        label1 = ttk.Label(frame3, text="Marks in Subject 1:")
        label1.grid(row=0, column=0, padx=10, pady=10)  # Place label in grid
        input1 = ttk.Entry(frame3)
        input1.grid(row=0, column=1, padx=10, pady=10)  # Place input box next to label
    
        # Create label and entry for Subject 2
        label2 = ttk.Label(frame3, text="Marks in Subject 2:")
        label2.grid(row=1, column=0, padx=10, pady=10)  # Place label in grid
        input2 = ttk.Entry(frame3)
        input2.grid(row=1, column=1, padx=10, pady=10)  # Place input box next to label
    
        # Create label and entry for Subject 3
        label3 = ttk.Label(frame3, text="Marks in Subject 3:")
        label3.grid(row=2, column=0, padx=10, pady=10)  # Place label in grid
        input3 = ttk.Entry(frame3)
        input3.grid(row=2, column=1, padx=10, pady=10)  # Place input box next to label
    
        label4 = ttk.Label(frame3, text="Marks in Subject 4:")
        label4.grid(row=3, column=0, padx=10, pady=10)  # Place label in grid
        input4 = ttk.Entry(frame3)
        input4.grid(row=3, column=1, padx=10, pady=10)  # Place input box next to label
        
        label5 = ttk.Label(frame3, text="Marks in Subject 4:")
        label5.grid(row=4, column=0, padx=10, pady=10)  # Place label in grid
        input5 = ttk.Entry(frame3)
        input5.grid(row=4, column=1, padx=10, pady=10)  # Place input box next to label
       
       
        # Create a Button to trigger the input processing
        submit_button = ttk.Button(frame3, text="Submit", command=lambda:get_marks_and_percent())
        submit_button.grid(row=5, column=1, padx=10)
            

# Function to retrieve the values and calculate percentage
def get_marks_and_percent1():

        s1 = float(input1.get())
        s2 = float(input2.get())
        s3 = float(input3.get())
        
        # Create an object of grade1 and calculate percentage
        obj1 = grade1()
        obj1.percetage_calculation(s1, s2, s3)
def get_marks_and_percent2():
        s1 = float(input1.get())
        s2 = float(input2.get())
        s3 = float(input3.get())
        s4 = float(input4.get())
        
        # Create an object of grade2 and calculate percentage
        obj1 = grade2()
        obj1.percetage_calculation(s1, s2, s3,s4)
def get_marks_and_percent3():
        s1 = float(input1.get())
        s2 = float(input2.get())
        s3 = float(input3.get())
        s4 = float(input4.get())
        s5 = float(input5.get())
        
        # Create an object of grade3 and calculate percentage
        obj1 = grade3()
        obj1.percetage_calculation(s1, s2, s3,s4,s5)





# Class for Grade 1 calculation
class grade1():
    def percetage_calculation(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.grade = "Grade 1"
        self.percentage = (self.s1 + self.s2 + self.s3) / 300 * 100
        
        # Frame 4: -------------------------------------
        frame4 = Frame(root, bg="blue", bd=5, relief="groove")  # Create the frame with a background color
        frame4.pack(fill="both")  # Add the frame to the main window and fill both

        label3 = Label(frame4, text=f"Percentage for {self.grade} is {self.percentage:.2f}%.", bg="lightblue", bd=0)
        label3.pack(pady=10)  # Added padding for better spacing
# Class for Grade 2 calculation
class grade2():
    def percetage_calculation(self, s1, s2, s3,s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.grade = "Grade 2"
        self.percentage = (self.s1 + self.s2 + self.s3+self.s4) / 400 * 100
        
        # Frame 4: -------------------------------------
        frame4 = Frame(root, bg="blue", bd=5, relief="groove")  # Create the frame with a background color
        frame4.pack(fill="both")  # Add the frame to the main window and fill both

        label3 = Label(frame4, text=f"Percentage for {self.grade} is {self.percentage:.2f}%.", bg="lightblue", bd=0)
        label3.pack(pady=10)  # Added padding for better spacing
# Class for Grade 3 calculation
class grade3():
    def percetage_calculation(self, s1, s2, s3,s4,s5):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5      
        self.grade = "Grade 3"
        self.percentage = (self.s1 + self.s2 + self.s3 + self.s4 + self.s5) / 500 * 100
        
        # Frame 4: -------------------------------------
        frame4 = Frame(root, bg="blue", bd=5, relief="groove")  # Create the frame with a background color
        frame4.pack(fill="both")  # Add the frame to the main window and fill both

        label3 = Label(frame4, text=f"Percentage for {self.grade} is {self.percentage:.2f}%.", bg="lightblue", bd=0)
        label3.pack(pady=10)  # Added padding for better spacing


root.mainloop()
