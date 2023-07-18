import tkinter as tk

def calculate_area():
    try:
        radius = float(entry.get())
        area = 3.14 * radius ** 2
        result_label.config(text=f"The area of your circle is {area:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Circle Area Calculator")

label = tk.Label(root, text="Enter circle radius:")
label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
