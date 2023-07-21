word=input("Enter word")
print("Original String:",word)

# len of str
size=len(word)

print("Printing only even index chars")
for i in range (0,size-1,2):
  print("index[",i,"]",word[i])



#Using LIST another method

word=input("Enter a word")
print("Original  String:",word)

#using LIST
#convert str --> list
#pick only even index chars

x=list(word)
for i in x[0::2]:
    print(i)
