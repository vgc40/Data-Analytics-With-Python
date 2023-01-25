from sys import argv
script,file_source,file_destination = argv

file_original = open(file_source)
file_content_original = file_original.read()

file_copy = open(file_destination, mode = 'w')

print(file_content_original, file = file_copy)

file_original.close()
file_copy.close()