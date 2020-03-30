
with open("Integertask.py","r") as f: #using this you do not need to close the file manually using command f.close()
    print(f.readline())

print (" Its the end of the world as we know it")# since it is not indented to the top piece of code it is independent of the file
# file is considered closed after the print function above has being called


with open ("Integertask.py","r") as f:
    for line in f:
        print(line, end="")

