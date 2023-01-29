from sys import argv

if len(argv) < 4 or len(argv) > 4:
    print("The code needs 4 input arguments, please check that the number of aguments inputted is correct")
else:
    print("This script is named {}".format(argv[0]))
    print("  The value of argument 1 is:", argv[1])
    print("  The value of argument 2 is:", argv[2])
    print("  The value of argument 3 is:", argv[3])

