import sys #Import this package that contains functions useful for managing
#Exceptions in errors.

try:#try command to determine if file exists it is opened and read.
    with open (sys.argv[1]) as f:
        print(f.read())

except:#Unless file does no exist then we printed error explaining why to an user that 
    #might be less experienced in spotting errors and reasons for them.
    print ("File"+ sys.argv[1]+"does not exist , you idiot.")


