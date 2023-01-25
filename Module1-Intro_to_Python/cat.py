from sys import argv
script,file_name = argv

file = open(file_name) # Allows you to get access to the file
file_content = file.read() # This reads the whole file

print(file_content) # This prints the file

file.close()
