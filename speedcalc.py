import tkinter as tk
from tkinter import Label, Entry, Button, Checkbutton, StringVar, messagebox
from PIL import Image, ImageTk

#Point systems
def points(speed_diff):
    if 6 <= speed_diff <= 10:
        return 2
    elif 11 <= speed_diff <= 15:
        return 3
    elif 16 <= speed_diff <= 25:
        return 4
    elif 26 <= speed_diff <= 30:
        return 5
    elif speed_diff >= 31:
        return "5 & PennDoT Hearing"
    else:
        return 0

#Define SubSection
def sub_sec(speed_limit):
    if speed_limit == 35:
        return "(a)(1)"
    elif speed_limit >= 65:
        return "(a)(1.1)"
    elif speed_limit == 25:
        return "(a)(1.2)"
    elif speed_limit == 55:
        return "(a)(2)"
    else:
        return "(a)(3)"

#Define general costs associated with ticket
def other_costs():
    jcpatj = 33.25
    ems = 20
    court = 48.50
    return jcpatj, ems, court

#Surcharge changes with speed difference
def surcharge(speed_diff):
    if speed_diff <= 15:
        return 45
    elif 16 <= speed_diff <= 25:
        return 60
    elif speed_diff >= 26:
        return 75

#Initial fine depending on speed zone
def initial_fine(speed_limit):
    if speed_limit >= 65:
        return 42.50
    else:
        return 35.0


def calculate_fine():
    try:
        speed_limit = int(speed_limit_entry.get())
        veh_speed = int(veh_speed_entry.get())
        safezone = safezone_var.get()

        if veh_speed <= speed_limit:
            result_label.config(text="Vehicle was within the posted speed limit.")
        else:
            speed_diff = veh_speed - speed_limit
            fine_speed = max(speed_diff - 5, 0) * 2
            jcpatj, ems, court = other_costs()
            surg = surcharge(speed_diff)
            fine = initial_fine(speed_limit) + fine_speed
            if safezone == 'yes':
                fine *= 2
            total_fine = fine + jcpatj + ems + court + surg

            result_text = (
                f"Fine: ${fine}\n"
                f"EMS: ${ems}\n"
                f"Surcharge: ${surg}\n"
                f"Court Costs: ${court}\n"
                f"ACPATJ: ${jcpatj}\n"
                f"Total Due: ${total_fine}\n\n"
                f"Points: {points(speed_diff)}\n"
                f"Box 26: 75\n"
                f"Box 27: 3362\n"
                f"Box 28: {sub_sec(speed_limit)}"
            )
            result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid integer values for speed limit and vehicle speed.")

# Display window
root = tk.Tk()
root.title("Speeding Ticket Calculator")

# Create and place widgets
Label(root, text="Speed Limit:").grid(row=0, column=0, padx=10, pady=10)
speed_limit_entry = Entry(root)
speed_limit_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Vehicle Speed:").grid(row=1, column=0, padx=10, pady=10)
veh_speed_entry = Entry(root)
veh_speed_entry.grid(row=1, column=1, padx=10, pady=10)

safezone_var = StringVar(value='no')
safezone_check = Checkbutton(root, text="Violation in School Zone or Active Work Zone", variable=safezone_var, onvalue='yes', offvalue='no')
safezone_check.grid(row=2, column=1, padx=10, pady=10)

calculate_button = Button(root, text="Calculate", command=calculate_fine, bg="#87cefa")
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

