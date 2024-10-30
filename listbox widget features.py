import tkinter as tk
from tkinter import messagebox

def show_selection():
    '''
    This function displays the currently selected item in the listbox.
    '''
    selected_items = lb.curselection()
    if selected_items:
        selected_text = lb.get(selected_items[0])
        messagebox.showinfo("Selection", f"You selected: {selected_text}")
    else:
        messagebox.showwarning("No selection", "Please select an item.")

def launch_listbox():
    '''
    This function creates and launches a widget listbox.
    '''
    global lb  # Declare as global to access it in the show_selection function
    lb = tk.Listbox(window, wrap=tk.WORD)

    # Add some items to the listbox
    for item in ["Apple", "Banana", "Orange", "Grape", "Mango"]:
        lb.insert(tk.END, item)
    
    lb.pack()

    # Add a button to show the selected item
    show_button = tk.Button(window, text='Show Selection', command=show_selection)
    show_button.pack()

# Create main window
window = tk.Tk()
window.title('Main Window')
window.geometry('900x800')

# Launch the listbox widget
launch_listbox()

# Run the application
window.mainloop()