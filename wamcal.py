import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("WAM CALCULATOR")
window.geometry("1430x900")

# Fonts for labels and entries
label_font = ("Courier New", 20, "bold", "italic")
entry_font = ("Courier New", 20)

# Serial number counter
serial_num = 2  # Starts at 2 to avoid overlapping with header row

# Frame to hold user inputs -> major, course code, credits, marks
input_frame = tk.Frame(window)
input_frame.pack(pady=10, fill="x")

# Header labels
tk.Label(input_frame, text="Major", font=label_font, anchor="center", width=25).grid(row=0, column=0, padx=10, pady=10)
major_entry = tk.Entry(input_frame, font=entry_font, width=25, justify="center")
major_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(input_frame, text="Serial Number", font=label_font, anchor="center", width=15).grid(row=1, column=0, padx=10, pady=10)
tk.Label(input_frame, text="Course Code", font=label_font, anchor="center", width=25).grid(row=1, column=1, padx=10, pady=10)
tk.Label(input_frame, text="Credit", font=label_font, anchor="center", width=15).grid(row=1, column=2, padx=10, pady=10)
tk.Label(input_frame, text="Marks", font=label_font, anchor="center", width=15).grid(row=1, column=3, padx=10, pady=10)

# List to store dynamic rows
entries = []

def add_course():
    """Add a new row for course entry."""
    global serial_num

    # Serial number (always display current count)
    sr_label = tk.Label(input_frame, text=str(serial_num - 1), font=entry_font, anchor="center", width=15)
    sr_label.grid(row=serial_num, column=0, padx=10, pady=5)

    # Course code
    course_code_entry = tk.Entry(input_frame, font=entry_font, width=25, justify="center")
    course_code_entry.grid(row=serial_num, column=1, padx=10, pady=5)

    # Credit
    credit_entry = tk.Entry(input_frame, font=entry_font, width=15, justify="center")
    credit_entry.grid(row=serial_num, column=2, padx=10, pady=5)

    # Marks
    mark_entry = tk.Entry(input_frame, font=entry_font, width=15, justify="center")
    mark_entry.grid(row=serial_num, column=3, padx=10, pady=5)

    # Save the row for future access
    entries.append([sr_label, course_code_entry, credit_entry, mark_entry])

    # Increment the serial counter
    serial_num += 1

def remove_course():
    """Remove the latest course entry row."""
    global serial_num

    if serial_num > 2:
        # Remove the last row of widgets
        last_row = entries.pop()  # Remove and retrieve the last set of widgets
        for widget in last_row:
            widget.grid_forget()  # Remove each widget from the grid

        # Decrement the serial counter
        serial_num -= 1

def grades():
    """Calculate the weighted average mark (WAM)."""
    total_weighted_marks = 0
    total_credits_value = 0

    for row in entries:
        try:
            credits = float(row[2].get())  # Credits entry is in the 3rd column
            marks = float(row[3].get())  # Marks entry is in the 4th column
            total_weighted_marks += marks * credits
            total_credits_value += credits
        except ValueError:
            print(f"Invalid input in marks or credits field: Marks={row[3].get()}, Credits={row[2].get()}")

    if total_credits_value > 0:
        wam = total_weighted_marks / total_credits_value
        return wam
    else:
        return None

def calculation():
    wam = grades()
    if wam is not None:
        result_label.config(text=f"Calculated WAM: {wam:.2f}")
    else:
        result_label.config(text="Invalid input. Please check your credits and marks.")

# Initialize the first row as default
add_course()

# Buttons to add or remove rows
add_button = tk.Button(window, text="Add Course", font=label_font, bg="blue", fg="green", command=add_course)
add_button.pack(pady=10)

remove_button = tk.Button(window, text="Remove Course", font=label_font, bg="blue", fg="red", command=remove_course)
remove_button.pack(pady=10)

calculation_button = tk.Button(window, text="Calculate WAM", font=label_font, bg="blue", fg="navy", command=calculation)
calculation_button.pack(pady=10)

# Result box to display the WAM
result_frame = tk.Frame(window)
result_frame.pack(pady=20)

result_label = tk.Label(result_frame, text="Calculated WAM will appear here", font=("Courier New", 22, "bold"), fg="black", bg="white", relief="solid", padx=20, pady=10)
result_label.pack()

# Run the Tkinter main event loop
window.mainloop()
