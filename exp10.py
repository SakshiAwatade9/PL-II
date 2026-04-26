#Simple GUI window
'''import tkinter as tk

# Create main window
root = tk.Tk()

# Set window title
root.title("Simple GUI Window")

# Set window size
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Hello, Welcome to Tkinter GUI!", font=("Arial", 14))
label.pack(pady=20)

# Add a button
def on_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=10)

# Run the application
root.mainloop()

#GUI calculator

import tkinter as tk
def calculate():
    try:
        result=eval(entry.get())
        output.config(text="Result:"+str(result))
    except:
        output.config(text="Error")
root=tk.Tk()
root.title("Calculator")
entry=tk.Entry(root,width=80)
entry.pack() 
btn=tk.Button(root,text="Calculate", command=calculate) 
btn.pack()
output=tk.Label(root, text="Result:") 
output.pack()
root.mainloop()

#Student information form

import tkinter as tk

def submit():
    print("Name:", name.get())
    print("Roll No.:", roll.get())

root = tk.Tk()
root.title("Student Form")

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Roll No").pack()   # FIXED HERE
roll = tk.Entry(root)
roll.pack()

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()

#Line plot
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,25]

plt.plot(x,y)
plt.title("Line Plot")
plt.show()

#Bar Chart

import matplotlib.pyplot as plt

names=["A","B","C"]
marks=[80,90,70]

plt.bar(names, marks)
plt.title("Bar Chart")
plt.show()

#Histogram
import matplotlib.pyplot as plt

data=[10,20,30,30,40,40]
plt.hist(data)
plt.title("Histogram")
plt.show()

#Pie chart
import matplotlib.pyplot as plt
labels=["Python","Java","C++"]
sizes=[40,20,40]
plt.pie(sizes,labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

#Box plot
import matplotlib.pyplot as plt
data=[1,2,3,4,5]
plt.boxplot(data)
plt.title("Box plot")
plt.show()

#Plot with Labels and legend

import matplotlib.pyplot as plt
x=[1,2,3]
y1=[10,20,30]
y2=[15,25,35]

plt.plot(x,y1,label="Line 1")
plt.plot(x,y2,label="Line 2")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()'''

import matplotlib.pyplot as plt

# Lists to store data
x = []
y = []

# Read data from file
with open("C:/Users/GCEK3/OneDrive/Desktop/Sakshi/data.txt", "r") as file:
    for line in file:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))

# Plot data
plt.plot(x, y, marker='o')
plt.title("Data Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

# Show graph
plt.show()