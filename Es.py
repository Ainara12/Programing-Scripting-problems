

# Ainara Ruiz Castillo
#With this program we are able to read in a text file and output the number of "e's" it contains. 
#Taking as reference the information in Real Python: https://realpython.com/read-write-files-python/ and also having consulted
#https://realpython.com/python-strings/.


with open ("testtext", "r") as reader: #First I opened example text file "testtext" which I have created in this directory
    text = reader.read() #in read mode and definde variables
    text.count ("e") # I defined text count for "e" letter
    print (text.count("e") ,"is the number of e's this text contains") #Print number of e's counted in file.


print ("Thanks for using my code")
