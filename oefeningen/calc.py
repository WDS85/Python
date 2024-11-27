import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Haal de waarden uit de invoervelden
        x = float(entry_x.get())
        y = float(entry_y.get())
        operator = entry_operator.get()

        # Voer de bewerking uit op basis van de operator
        if operator == "+":
            result = x + y
        elif operator == "-":
            result = x - y
        elif operator == "*":
            result = x * y
        elif operator == "/":
            if y != 0:
                result = x / y
            else:
                messagebox.showerror("Fout", "Delen door nul is niet toegestaan.")
                return
        else:
            messagebox.showerror("Fout", "De verkeerde operator werd gebruikt.")
            return

        # Toon het resultaat
        label_result.config(text=f"Resultaat: {x} {operator} {y} = {result}")
    except ValueError:
        messagebox.showerror("Fout", "Voer geldige getallen in.")

# Maak het hoofdvenster
root = tk.Tk()
root.title("Rekenmachine")

# Maak invoervelden en labels
label_x = tk.Label(root, text="Eerste getal:")
label_x.grid(row=0, column=0)
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1)

label_y = tk.Label(root, text="Tweede getal:")
label_y.grid(row=1, column=0)
entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1)

label_operator = tk.Label(root, text="Operator (+, -, *, /):")
label_operator.grid(row=2, column=0)
entry_operator = tk.Entry(root)
entry_operator.grid(row=2, column=1)

# Knop om te berekenen
button_calculate = tk.Button(root, text="Bereken", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2)

# Label voor het resultaat
label_result = tk.Label(root, text="Resultaat: ")
label_result.grid(row=4, column=0, columnspan=2)

# Start het venster
root.mainloop()
