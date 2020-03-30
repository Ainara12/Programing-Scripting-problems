# With this program we are going to ask user to add
# a sentence in which characters shown are every second letter in reverse order

Addingsentence=str(input("Enter a sentence here (please use inverted commas): "))

invertorder= Addingsentence[::-2]

print ("Your sentence is:", invertorder)

#Used this sentence as example: The quick brown fox jumps over the lazy dog, which
#should show as: '.o zletrv pu o wr cu h'
