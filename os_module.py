import os

# Get current working directory
print("printing current directory")
print(os.getcwd())

#change directory
# os.chdir("c:/Users/MD Towfik Omer/OneDrive/Documents")

# list files in current directory
print("Before:")
print(os.listdir())

# making one directory
# os.mkdir("demo_folder") 

# making mulitple directories
# os.makedirs("parent/child/grandchild")   

# remove empty directory
# os.rmdir("demo_folder")

# remove multiple/nested directory
# os.removedirs("parent/child/grandchild

# Rename a file
# os.rename("old_file.txt", "new_file.txt")

# delete a file
# os.remove("file_name.txt")

# Get environment variable
print(os.environ.get("PATH"))

# Set an environment variable
os.environ["MY_VAR"] = "HelloWorld"
print(os.environ["MY_VAR"])


