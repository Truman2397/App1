# Import Library
from tkinter import *

# Create Tkinter Object
root = Tk()

# Set Title
root.title('Auto Select and Search')

# Set Geometry
root.geometry("400x300")

# Update the listbox
def update_listbox(data):
  # Clear the listbox
  list_box.delete(0, END)

  # Add programming_lan to listbox
  for item in data:
    list_box.insert(END, item)

# Update entry box with listbox clicked
def update(e):
  # Delete entry box
  entry.delete(0, END)

  # Add clicked list item to entry box
  entry.insert(0, list_box.get(ANCHOR))

# Check entry box vs listbox
def check(e):
  # get typed text
  typed_text = entry.get()

  if typed_text == '':
    data = programming_lan
  else:
    data = []
    for item in programming_lan:
      if typed_text.lower() in item.lower():
        data.append(item)

  # update our listbox
  update_listbox(data)        

# Create a label
label = Label(root, text="Auto Select and Search",font=("Helvetica", 14))
label.pack(pady=20)

# Create an entry box
entry = Entry(root, font=("Helvetica", 20))
entry.pack()

# Create a listbox
list_box = Listbox(root, width=50)
list_box.pack(pady=40)

# Programming Language List
programming_lan = ["Python","Javascript","C++","Java","PHP","Kotlin"]

# Add the programming_lan to our list
update_listbox(programming_lan)

# Create a binding on the listbox
list_box.bind("<<ListboxSelect>>", update)

# Create a binding on the entry box
entry.bind("<KeyRelease>", check)

# Execute Tkinter
root.mainloop()
