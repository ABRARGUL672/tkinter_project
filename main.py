# import tkinter as tk

# def on_button_click():
#     label.config(text="Button Clicked!")

# # Create the main window
# root = tk.Tk()
# root.title("Menu Demonstration")

# # Create a label
# label = tk.Label(root, text="hi, Tkinter!")
# label.pack(pady=10)

# Create a button
# button = tk.Button(root, text="Click Me", command=on_button_click)
# button.pack(pady=10)

# Start the Tkinter event loop
# root.mainloop()


# import tkinter as tk
# from tkinter import Menu

# #Create the main window

# root = tk.Tk()
# root.title("Menu Demonstration")

# #create menu bar

# menubar =Menu(root)
# root.config(menu=menubar)

# # Adding file menu and commands

# file = Menu(menubar,tearoff=0)
# menubar.add_cascade(label='File',menu=file)
# file.add_command(label='new_file',command=None)
# file.add_command(label='save',command=None)
# file.add_command(label='save as',command=None)
# file.add_command(label='run',command=None)
# file.add_command(label='Exit',command = None)


# # # Add the "Edit" menu

# edit =Menu(menubar,tearoff=0)
# menubar.add_cascade(label='Edit',menu=edit)
# edit.add_command(label='cut',command=None)
# edit.add_command(label='copy',command=None)
# edit.add_command(label='paste',command=None)
# edit.add_command(label='select all',command=None)
# edit.add_separator()
# edit.add_command(label='find...',command=None)
# edit.add_command(label='find again',command=None)

# help = Menu(menubar,tearoff=0)
# menubar.add_cascade(label='Help',menu = help)
# help.add_command(label='help',command=None)
# root.config(menu=menubar)

# root.mainloop()



# import tkinter as tk
# Define functions for menu actions
# def open_file():
#     messagebox.showinfo("Open", "Open File option selected")

# def save_file():
#     messagebox.showinfo("Save", "Save File option selected")

# def exit_app():
#     root.quit()

# Create the main window
# root = tk.Tk()
# root.title("Tkinter App with Menu")

# Create a Menu bar
# menubar = Menu(root)
# root.config(menu=menubar)

# # Add the "File" menu
# file= Menu(menubar, tearoff=0)
# menubar.add_cascade(label="File", menu=file)
# file.add_command(label="Open", command=None)
# file.add_command(label="Save", command=None)
# file.add_separator()
# file.add_command(label="Exit", command=None)

# # Add the "Edit" menu
# edit = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="Edit", menu=edit)
# edit.add_command(label="Cut", command=None)
# edit.add_command(label="Copy", command=None)
# edit.add_command(label="Paste", command=None)

# # Start the Tkinter event loop
# root.mainloop()


# import tkinter as tk
# from tkinter import Menu, filedialog, Text

# # Create the main window
# root = tk.Tk()
# root.title("Menu Demonstration")

# # Text widget for demonstrating cut, copy, and paste
# text_area = Text(root, wrap='word')
# text_area.pack(expand='yes', fill='both')

# # Function definitions for menu commands
# def new_file():
#     text_area.delete(1.0, tk.END)  # Clears the current text in the text area

# def save_file():
#     file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
#                                              filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
#     if file_path:
#         with open(file_path, 'w') as file:
#             file.write(text_area.get(1.0, tk.END))  # Write the current text to the file

# def run_file():
#     # Placeholder for running the file (you can add logic to run code, scripts, etc.)
#     print("Run command executed!")

# def cut_text():
#     text_area.event_generate("<<Cut>>")

# def copy_text():
#     text_area.event_generate("<<Copy>>")

# def paste_text():
#     text_area.event_generate("<<Paste>>")

# def find_text():
#     # Placeholder for find functionality
#     print("Find command executed!")

# def exit_app():
#     root.quit()

# # Create menu bar
# menubar = Menu(root)
# root.config(menu=menubar)

# # Add "File" menu and commands
# file_menu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='New File', command=new_file)
# file_menu.add_command(label='Save', command=save_file)
# file_menu.add_command(label='Run', command=run_file)
# file_menu.add_separator()
# file_menu.add_command(label='Exit', command=exit_app)

# # Add "Edit" menu and commands
# edit_menu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=edit_menu)
# edit_menu.add_command(label='Cut', command=cut_text)
# edit_menu.add_command(label='Copy', command=copy_text)
# edit_menu.add_command(label='Paste', command=paste_text)
# edit_menu.add_separator()
# edit_menu.add_command(label='Find', command=find_text)

# # Add "Help" menu (currently no functionality, but you can add something like Help contents)
# help_menu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Help', menu=help_menu)
# help_menu.add_command(label='Help', command=lambda: print("Help Command"))

# # Run the application
# root.mainloop()

# import tkinter as tk
# from tkinter import Menu

# #create a window
# root = tk.Tk()
# root.title('welcome')
# # print("\n\n\n\nroot",tk)
# # center_window(400,400)

# #create a label
# label = tk.Label(root,text ='hello')
# label.pack(pady=30)

# # #create a butt0n 
# # button =tk.Button(root,text ='click')
# # button.pack(pady=20)

# #create a menubar
# menubar =Menu(root)
# root.config(menu=menubar)

# file =Menu(menubar,tearoff=0)
# menubar.add_cascade(label = 'File',menu=file)
# file.add_command(label='open',command=None)
# file.add_command(label ='copy',command=None)

# edit =Menu(menubar,tearoff=0)
# menubar.add_cascade(label='Edit',menu=edit)
# edit.add_command(label='cut',command=None)

# root.mainloop()


import tkinter as tk
# tk._test()
root = tk.Tk()
root.title('welcome')
# def on_click():
#     btn.config(text='clicked')

# lbl = tk.Label(root,text='abc')
# lbl.grid(row=3,column=2,pady = 4)


# btn = tk.Button(root,text='abrar',command =on_click)
# btn.grid(row=7,column=6)
def add_to_list(Event = None):
    text=entry.get()
    if text:
       list.insert(tk.END,text)
       entry.delete(0,tk.END)

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

frame =tk.Frame(root)
frame.grid(row=0,column=0,sticky ='nsew')
frame.columnconfigure(0,weight=1)
frame.rowconfigure(0,weight=1)

entry =tk.Entry(frame)
entry.grid(row=0,column=0,sticky='ew')

entry.bind("<Return>",add_to_list)

btn = tk.Button(frame,text='add',command=add_to_list)
btn.grid(row =0,column=1)
list = tk.Listbox(frame)
list.grid(row=1 , column=0 ,columnspan=3,sticky='ew')
root.mainloop()