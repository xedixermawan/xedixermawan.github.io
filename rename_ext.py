import os 
import json 
import shutil

def inExceptionList(fname):
	exceptionList = { "root.json", "dir_metadata.json", "rename_ext.json", "rename_ext.py" }
	if fname in exceptionList:
		return True
	return False

def rename_ext_file(path): 
	# Initialize the result dictionary with folder
	# name, type, and an empty list for children
	name = os.path.basename(path)

	# Iterate over the entries in the directory 
	for entry in os.listdir(path): 
	# Create the full path for the current entry 
		entry_path = os.path.join(path, entry) 
		#print(entry_path)
		# If the entry is a directory, recursively call the function 
		if os.path.isdir(entry_path): 
			rename_ext_file(entry_path)
		# If the entry is a file, create a dictionary with name and type 
		else:
			if (inExceptionList(entry) == False):
				old_file = entry_path
				split_name =  os.path.splitext( entry_path )
				print(split_name[0])
				new_file = split_name[0] + ".md"
				if os.path.isfile(new_file) == False: # check if file exist
					os.rename(old_file, new_file)
				print(old_file)


# Specify the path to the folder you want to create the JSON for 
folder_path = './post'
# Call the function to create the JSON representation 
rename_ext_file(folder_path)