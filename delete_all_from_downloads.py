## This is code to clean out my downloads folder using the os module ## 

# Import os module, to allow interaction in operating system
import os

# opens the directory to my downloads folder
directory_path = '/users/Colby/Downloads'

files_deleted = False

print("The Pdf Files in ", directory_path)

# A loop that returns the entries in my Downloads folder
# Then joins the name of the file specifically in the Downloads folder
# Uses os.remove to delete the file

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    
    if  os.path.isfile(file_path):
        os.remove(file_path)
        files_deleted = True
        print(f"Deleted: {file_path}")

if files_deleted:
    print("Files have been deleted")
else:
    print('No files have been deleted')
