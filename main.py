

old_file_location = "GSC-OLD-DISAVOW-CANALWALK.txt"
new_file_location = "SEM-NEW-DISAVOW-CANALWALK.txt"

with open(old_file_location) as old_file:
    old_content = old_file.readlines()
    old_content_stripped = [line.strip() for line in old_content]


with open(new_file_location) as new_file:
    new_content = new_file.readlines()
    new_content_stripped = [line.strip() for line in new_content]

# Getting the new lines that were added
new_domains = []
for line in new_content_stripped:
    if line not in old_content_stripped:
        new_domains.append(line)

# Printing the new domains
print("New disavowed domains: (Paste these in the Negative SEO sheet) \n")
for i in new_domains:
    print(i)

# Total new domains added
print(f"\nTotal new domains disavowed: {len(new_domains)}")

# Writing a text file with the OLD and NEW disavowed links to put in Google Search Console/
with open("NEW_DISAVOWED + OLD_DISAVOWED.txt", "w") as new_disavowed_old_disavowed:
    for i in old_content_stripped:
        new_disavowed_old_disavowed.writelines(f"{i}\n")

    for j in new_domains:
        new_disavowed_old_disavowed.writelines(f"{j}\n")


