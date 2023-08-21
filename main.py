import tkinter as tk
from tkinter import filedialog

old_file_location = "OLD_GSC_DIASVOW_SOMERSET - Copy.txt"
new_file_location = "NEW_SEM_DISAVOW_SOMERSET.txt"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BACKGROUND_COLOR = "#ED2437"
BUTTON_COLOR = ""
LABEL_COLOR = ""
TEXTBOX_COLOR = ""

global old_file_path, new_file_path


def center_window(window, width, height):
    """Function to center the main window"""
    window.update_idletasks()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


def on_old_button():
    print("Old Button Clicked")
    global old_file_path

    old_file_path = filedialog.askopenfilename()
    if old_file_path:
        old_file_label.config(text=f"Selected File: {old_file_path}")
    else:
        old_file_label.config(text="No File Selected")


def on_new_button():
    print("Old Button Clicked")
    global new_file_path

    new_file_path = filedialog.askopenfilename()
    if new_file_path:
        new_file_label.config(text=f"Selected File: {new_file_path}")
    else:
        old_file_label.config(text="No File Selected")


def process():
    print("Process button clicked")
    global old_file_path, new_file_path

    # Opening the Old File
    with open(old_file_path) as old_file:
        old_content = old_file.readlines()
        old_content_stripped = [line.strip() for line in old_content]

    # Opening the New File
    with open(new_file_path) as new_file:
        new_content = new_file.readlines()[2:-2]  # Removing comments from SEM file
        new_content_stripped = [line.strip() for line in new_content]

    # Getting the new lines that were added
    new_domains = []
    for line in new_content_stripped:
        if line not in old_content_stripped:
            new_domains.append(line)
            new_domains_textbox.insert(tk.END, f"{line}\n")
    # new_domains_textbox.insert(tk.END, new_domains)

    # Printing the new domains
    print("New disavowed domains: (Paste these in the Negative SEO sheet) \n")
    for i in new_domains:
        print(i)

    # Total new domains added
    print(f"\nTotal new domains disavowed: {len(new_domains)}")

    # Writing a text file with the OLD and NEW disavowed links to put in Google Search Console
    with open("NEW_DISAVOWED + OLD_DISAVOWED.txt", "w") as new_disavowed_old_disavowed:
        for i in old_content_stripped:
            new_disavowed_old_disavowed.writelines(f"{i}\n")

        for j in new_domains:
            new_disavowed_old_disavowed.writelines(f"{j}\n")


# Creating the GUI
root = tk.Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.config(bg=BACKGROUND_COLOR)

client_label = tk.Label(root, text="Which Client is This For?")
client_label.pack()

client_entry = tk.Entry(root)
client_entry.pack()

# Old File Stuff
old_file_label = tk.Label(root, text="Old File Location", padx=20, pady=20)
old_file_label.pack()

old_file_button = tk.Button(root, text="Select File Location", command=on_old_button)
old_file_button.pack()


# New File Stuff
new_file_label = tk.Label(root, text="New File Location", padx=20, pady=20)
new_file_label.pack()

new_file_button = tk.Button(root, text="Select File Location", command=on_new_button)
new_file_button.pack(padx=20, pady=20)

# Processing the files
process_button = tk.Button(root, text="Process", command=process, width=20, height=5)
process_button.pack()


# Textbox for New Domains
new_domains_textbox = tk.Text(root, height=50, width=50)
new_domains_textbox.pack()




if __name__ == '__main__':
    center_window(root, WINDOW_WIDTH, WINDOW_HEIGHT)
    root.mainloop()
