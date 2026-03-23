import tkinter as tk

# Functions
def press(key):
    entry_var.set(entry_var.get() + str(key))

def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def clear():
    entry_var.set("")

# Main window
root = tk.Tk()
root.title("Stylish Calculator")
root.geometry("400x550")
root.resizable(False, False)
root.configure(bg="#2E2E2E")  # Dark background

# Entry
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Helvetica", 28), bd=5, relief="ridge", justify="right", bg="#1E1E1E", fg="white", insertbackground='white')
entry.pack(fill='both', padx=10, pady=20, ipady=10)

# Button styling
button_style = {
    'font': ("Helvetica", 20, "bold"),
    'bd': 0,
    'fg': "white",
    'width': 4,
    'height': 2,
    'relief': "ridge",
    'activebackground': "#FF9500",
    'activeforeground': "white"
}

# Buttons layout
buttons = [
    ['C', '/', '*', '-'],
    ['7', '8', '9', '+'],
    ['4', '5', '6', '='],
    ['1', '2', '3', '.'],
    ['0']
]

# Create buttons
for r, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#2E2E2E")
    frame.pack(expand=True, fill='both')
    for c, button in enumerate(row):
        if button == "=":
            b = tk.Button(frame, text=button, bg="#FF9500", **button_style, command=equal)
        elif button == "C":
            b = tk.Button(frame, text=button, bg="#FF3B30", **button_style, command=clear)
        else:
            b = tk.Button(frame, text=button, bg="#505050", **button_style, command=lambda key=button: press(key))
        b.pack(side='left', expand=True, fill='both', padx=3, pady=3)

root.mainloop()