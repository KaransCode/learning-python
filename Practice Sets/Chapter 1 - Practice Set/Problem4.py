#  Printing the contents of a dir using os module in Python

# --- Program: List Files and Directories ---

# Step 1 : Importing Os module
import os 

# Step 2 : Specifying the Path 
# For which we have to list the directories

path = "E:/"

# Step 3 : Passing the path variable to dir_list
# function through os module's listdir method

dir_list = os.listdir(path) 

# Step 4 : Printing the list of directories

print("Files and directories in '", path, "' :") 
print(dir_list)

# --- Program Ends Here ---