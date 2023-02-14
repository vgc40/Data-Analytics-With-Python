from sys import argv

"""
    This program contains relevant steps for the class project
    Created by: Vanessa Garayburu-Caruso
   
"""
# Defining global variables as dictionaries following the exceptions to the rule
AREAS = {
    0: 'All',
    1: 'Rawah Wilderness Area',
    2: 'Neota Wilderness Area',
    3: 'Comanche Peak Wilderness Area',
    4: 'Cache la Poudre Wilderness Area'
}

COLUMNS = {
    0: 'Elevation',
    1: 'Aspect',
    2: 'Slope',
    3: 'Horizontal_Distance_To_Hydrology',
    4: 'Vertical_Distance_To_Hydrology',
    5: 'Horizontal_Distance_To_Roadways',
    6: 'Hillshade_9am',
    7: 'Hillshade_Noon',
    8: 'Hillshade_3pm',
    9: 'Horizontal_Distance_To_Fire_Points'
}

def get_stats(cx):
    '''
        This function allows you to calculate min, max and mmean values of a list of integers

        Parameters
        ----------
        cx : List of integers

        Returns
        -------
        List if integers where the first value is the min, the second is the maximun and the third one is the average

    '''
    minx = round(min(cx),2) # Use Python pre-made function for minimun value in a list
    maxx = round(max(cx),2) # Use Python pre-made function for maximun value in a list
    meanx = round(sum(cx)/len(cx),2) # Calculate mean as the sum of all the values in the list divided by the lenght of the list
                    # Note I use the round function to control for signifucant digits printed
    return [minx, maxx, meanx]

def main():
    """
    This function contains variables to run the program when running from command-line
    
    Parameters
    ----------
    None
  
    Returns
    -------
    Output file with print information of the mathematical operations of the columns in the dataset
    """

script, file_name = argv
file = open(file_name)

# Task 1: Calulate Min, Max and Mean of the first 10 columns in the dataset

# Step 1: read in a line and parse out as integers the values of the 10 columns in the 1st line
line = file.readline().split(",") # Reads a line
c0 = float(line[0]) # Column 1 Row 1
c1 = float(line[1])
c2 = float(line[2])
c3 = float(line[3])
c4 = float(line[4])
c5 = float(line[5])
c6 = float(line[6])
c7 = float(line[7])
c8 = float(line[8])
c9 = float(line[9])

# Step 2. Create a list that we can append on un a loop by reading in the sedond line and appending the numbers form the Step 1
line1 = file.readline().split(",") # Reads a line
c0 = [c0,float(line1[0])] # Column 1 row 2
c1 = [c1,float(line1[1])]
c2 = [c2,float(line1[2])]
c3 = [c3,float(line1[3])]
c4 = [c4,float(line1[4])]
c5 = [c5,float(line1[5])]
c6 = [c6,float(line1[6])]
c7 = [c7,float(line1[7])]
c8 = [c8,float(line1[8])]
c9 = [c9,float(line1[9])]
      

# Step 3. Now that we have created a list of integers in the previous steps we can use a loop to make append to the list all the values in the rest of the rows
for rows in file: 
    line2 = rows.split(",") # Reads a line
    c0.append(float(line2[0])) # Append to the c0 list the value in column one and row = rows
    c1.append(float(line2[1]))
    c2.append(float(line2[2]))
    c3.append(float(line2[3]))
    c4.append(float(line2[4]))
    c5.append(float(line2[5]))
    c6.append(float(line2[6]))
    c7.append(float(line2[7]))
    c8.append(float(line2[8]))
    c9.append(float(line2[9]))

# Step 4. Use the created function that calculates the Min, Max and Mean for each of the colums

# Step 5: Use the function to calculate the stats and also to write out into the output file
output_file = open("project_output.txt", mode = 'w') # Open and create an output file for writing
# Write the first line to explain the outputs that the user will see
output_file.write("The following lines contain stats for the first 10 columns of the dataset.\n")

lista = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9] # Make a list with all the lists from each column so it it easier to loop
# Setp 5.1: Loop across all of the elements in the list to run the function and read the outputs in the output file

for i in range(0,10):
    a = get_stats(lista[i]) # Runs function and stores the outputs into a which will be used to print to the output file. 
    output_file.write("{}, the Minimun value is {}, the Maximun is {} and the Mean is {}\n".format(COLUMNS[i],a[0],a[1],a[2])) # Uses format to format the output. Uses the COLUMNS global variable to pull the name of the column so it makes sense what numbers we are seeing
file.close() # Close file 

# Task 2: Calculate the same set of statistics but for each of the seven wilderness areas. The wilderness areas are identified in columns 11-14 of the data file.

output_file.write("\nThe following lines contain stats for each of the seven wilderness areas and each column.\n\n")

# Defining areas locally as an empty list
areas = {
    'All': [],
    'Rawah Wilderness Area': [],
    'Neota Wilderness Area': [],
    'Comanche Peak Wilderness Area' : [],
    'Cache la Poudre Wilderness Area' : []
} 

file = open("covtype.data") #opening the file again
#Step 6: Use a for loop to go through each of the rows in the dataset and categorize 
#the first 10 columns into the new lists them based on their wilderness area
for rows in file: 
    line = rows.split(',')    
    if float(line[10]) == 1:
         areas['Rawah Wilderness Area'].append(line[0:10])
    elif float(line[11]) == 1:
        areas['Neota Wilderness Area'].append(line[0:10])
    elif float(line[12]) == 1:
         areas['Comanche Peak Wilderness Area'].append(line[0:10])
    elif float(line[13]) == 1:
         areas['Cache la Poudre Wilderness Area'].append(line[0:10])
    elif (float(line[10]) == 1) and (float(line[11]) == 1) and (float(line[12]) == 1) and (float(line[13]) == 1):
         areas['All'].append(line[0:10])            

#Step 7: Now calculate the stats for each column within each wilderness area
x = [] # empty list used temporarly to assamble the list per column in the loop below
keys = list(areas.keys()) # Getting the wilderness area names
# Use 3 nested loops to loop around the wilderness areas (k), each of the columns one at the time (i) and create a list for each column inside each wilderness area to calculate stats (j)
for k in keys:
    length = len(areas[k])
    if length > 0: # This makes sure that the areas that we select to calculate stats has data
        for i in range(0,10):
            x = [] #resetting the counter of temp x in the loop before the next column
            for j in range(0,length):
                x.append(float(areas[k][j][i])) #Appending values from each column into a temp list
            a = get_stats(x)   # Saving stats in a 
            output_file.write("{}, Column {}.\nThe Minimun value is {}\nThe Maximun is {}\nThe Mean is {}\n".format(k,COLUMNS[i],a[0],a[1],a[2])) # Wring the results in teh putput file

output_file.close()

file.close()
               
if __name__ == "__main__":
    main()