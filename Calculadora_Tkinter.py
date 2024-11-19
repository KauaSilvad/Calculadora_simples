import tkinter as tk
def button_click(value):
    current = entry.get()
    
    if value.isdigit() or value in "+-*/.":
        entry.delete(0, tk.END)  
        entry.insert(tk.END, current + value)

def calculate():
    try:
        result = eval(entry.get()) 
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculadora")
root.config(bg='#333333')
entry = tk.Entry(root, width=16, font=("Poppins", 32), borderwidth=1, relief="solid", justify="right", bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def create_button(text,row, col, command):
    return tk.Button(root, text=text, width=5, height=2, font=("Poppins", 20), command=command, 
                     bg="#444444", fg="white", activebackground="#555555", activeforeground="white",
                     relief="flat", bd=0,)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        button = create_button(text, row, col, calculate)
    else:
        button = create_button(text, row, col, lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, padx=5, pady=5)


clear_button = create_button("C", 5, 0, clear)
clear_button.grid(row=5, column=0, columnspan=4, pady=10, padx=5)

root.mainloop()
