
#Practicing with opening and reading files taking as reference Realptyhon blog entry.
# Read and print the entire file line by line

with open("testtext", "a") as a_writer:
    a_writer.write("Hola fea")

with open ("testtext","r") as reader:
    print (reader.read(340))
    

