import datetime


CLIENT = "Woodlands"



OLD_FILE_LOCATION = "OLD-DISAVOW-Woodlands-GSC.txt"
NEW_FILE_LOCATION = "NEW-DISAVOW-Woodlands-SEM.txt"

def remove_duplicates(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

def get_current_date_and_time():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")


# Opening the Old File
with open(OLD_FILE_LOCATION) as old_file:
    old_content = old_file.readlines()
    print(f"Old content lines: {len(old_content)}")

    # Making a list of all lines in the old file and removing duplicates
    old_content_stripped = remove_duplicates(line.strip() for line in old_content)
    print(f"Old content lines after removing duplicates: {len(old_content_stripped)}")

    print(f"Total duplicates removed: {len(old_content) - len(old_content_stripped)}")

# Opening the New File
with open(NEW_FILE_LOCATION) as new_file:
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
with open(f"{CLIENT} NEW_DISAVOWED+OLD_DISAVOWED_{str(get_current_date_and_time())}.txt", "w") as new_disavowed_old_disavowed:
    for i in old_content_stripped:
        new_disavowed_old_disavowed.writelines(f"{i}\n")

    for j in new_domains:
        new_disavowed_old_disavowed.writelines(f"{j}\n")


