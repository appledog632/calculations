import tkinter as tk
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


root = tk.Tk()
root.title("GIRLY CALCULATIONS 🎀")
root.geometry("350x500")
root.configure(bg="#ffffff")

display = tk.Entry(root, font=('Comic Sans MS', 24), bd=10, insertwidth=4, width=14, borderwidth=4, bg="#ffe6f7")
display.grid(row=0, column=0, columnspan=4, pady=20)

button_font = ('Comic Sans MS', 18)
button_color = "#ffffff"  
button_border = "#000000" 
text_color = "#000000"  

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        action = clear
    elif text == '=':
        action = calculate
    else:
        action = lambda val=text: button_click(val)

    button = tk.Button(root, text=text, padx=20, pady=20, font=button_font, bg=button_color, fg=text_color, 
                       bd=4, relief="solid", highlightbackground=button_border, highlightthickness=2, 
                       command=action)
    button.grid(row=row, column=col, padx=10, pady=10)

root.mainloop()