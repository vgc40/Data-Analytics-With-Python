from sys import argv
from os.path import exists # Importing object exists from package os.path

script, num1, num2, num5, num3, num4, out_filename = argv #  Calculating and average

file_exists = exists(out_filename) # True or False weather the file exists or not
print("Does the output file exist? {}".format(file_exists))
print("Writing output to {}".format(out_filename))

out_file = open(out_filename, 'w') # Opening out_file returning a file object 
outdata = out_file # not necesary. Defining a new varible with out_file
print("Waiting... Type the RETURN key to continue")
input() # Allows user input but it's not storing it. Just waiting for the user. Indentation error occurs because Python is very strict with indentation. You have to be consistent and it might be thinking this is related to the function
      
answer = (float(num1) + float(num2) + float(num5) + float(num3) + float(num4)) / (len(argv) - 2) # Calculating an average of inputs

out_file.write("{:.2f}\n".format(answer)) # Writting the answer into out file and also formatting the number of digits in the answer that we want to print. 
print("\a") # \a is a esc "a" which is printing an alarm it will make a sound
out_file.close() # close file