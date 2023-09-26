import datetime
import tkinter as tk
from tkinter import filedialog

CLIENT = ""  # Initialize the client name as empty

def center_window(window, width, height):
    """Function to center the main window"""
    window.update_idletasks()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def remove_duplicates(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

def get_current_date_and_time():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

def process_files(client_name, old_file_location, new_file_location):
    # Opening the Old File
    with open(old_file_location) as old_file:
        old_content = old_file.readlines()
        print(f"Old content lines: {len(old_content)}")

        # Making a list of all lines in the old file and removing duplicates
        old_content_stripped = remove_duplicates(line.strip() for line in old_content)
        print(f"Old content lines after removing duplicates: {len(old_content_stripped)}")

        print(f"Total duplicates removed: {len(old_content) - len(old_content_stripped)}")

    # Opening the New File
    with open(new_file_location) as new_file:
        new_content = new_file.readlines()

        # Removing the "#" comments out and any blank spaces that might have been added
        new_content_stripped = [line.strip() for line in new_content if "#" not in line and not str.isspace(line)]

    # Getting the new lines that were added
    new_domains = []
    for line in new_content_stripped:
        if line not in old_content_stripped:
            new_domains.append(line)

    # Printing the new domains
    print("\nNew disavowed domains: (Paste these in the Negative SEO sheet)\n")
    for i in new_domains:
        print(i)

    # Total new domains added
    print(f"\nTotal new domains disavowed: {len(new_domains)}")

    # Writing a text file with the OLD and NEW disavowed links to put in Google Search Console
    output_filename = f"{client_name}_NEW_DISAVOWED+OLD_DISAVOWED_{get_current_date_and_time()}.txt"
    with open(output_filename, "w") as new_disavowed_old_disavowed:
        for i in old_content_stripped:
            new_disavowed_old_disavowed.writelines(f"{i}\n")

        for j in new_domains:
            new_disavowed_old_disavowed.writelines(f"{j}\n")

def select_old_file():
    old_file_location = filedialog.askopenfilename(title="Select Old File")
    old_file_entry.delete(0, tk.END)
    old_file_entry.insert(0, old_file_location)

def select_new_file():
    new_file_location = filedialog.askopenfilename(title="Select New File")
    new_file_entry.delete(0, tk.END)
    new_file_entry.insert(0, new_file_location)

def process_button_clicked():
    client_name = client_name_entry.get()
    old_file_location = old_file_entry.get()
    new_file_location = new_file_entry.get()
    if client_name and old_file_location and new_file_location:
        process_files(client_name, old_file_location, new_file_location)
    else:
        print("Please enter the client name and select both old and new files before processing.")

# Create the main window
window_width = 500
window_height = 350  # Slightly taller to accommodate the client name input

root = tk.Tk()
root.geometry()
root.title("File Processor")

# Label and Entry for Client Name
client_name_label = tk.Label(root, text="Client Name:")
client_name_label.pack()
client_name_entry = tk.Entry(root)
client_name_entry.pack()

# Label and Entry for Old File
old_file_label = tk.Label(root, text="Old File Location:")
old_file_label.pack()
old_file_entry = tk.Entry(root)
old_file_entry.pack()
old_file_button = tk.Button(root, text="Select Old File", command=select_old_file)
old_file_button.pack()

# Label and Entry for New File
new_file_label = tk.Label(root, text="New File Location:")
new_file_label.pack()
new_file_entry = tk.Entry(root)
new_file_entry.pack()
new_file_button = tk.Button(root, text="Select New File", command=select_new_file)
new_file_button.pack()

# Process Button
process_button = tk.Button(root, text="Process Files", command=process_button_clicked)
process_button.pack(pady=20)

if __name__ == '__main__':
    center_window(root, window_width, window_height)
    root.mainloop()

