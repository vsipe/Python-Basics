from collections import defaultdict
import re
#Key Words counter
#want to make a function that can get a paragraph and then count all of the words in that paragraph, and then put them in order from most used to least used. 

#let's start with the function that can get a paragraph as a string first



#counts the number of words in a string
def count_Words(input):
    counts = defaultdict(int)
    for word in re.findall('\w+', input):
        counts[word] += 1
    
    # want to reorder all of the top words in a job posting 
    # take out the Tos, thes and ands
    for word in list(counts): #must use list(counts) because you can't delete something that you're iterating through. 
        if word == 'and' or word == 'The' or word == 'the' or word == 'to' or word == 'with' or word == 'of':
            counts.pop(word) #deletes the word that matches the ones in the above if statement. 
     
    return counts

#make a function that organizes the capital letters
def capital_letters(input):
    counts = defaultdict(int)
    for word in re.findall('\w+', input):
        counts[word] += 1
    
    capital_list = []
    for word in counts:  
        if word.isupper():
            capital_list.append(word)
            
            #prints if something contains a capital letter
        elif word.istitle():
            capital_list.append(word)
            
    #how do I get this to still print the counts? I'm really not sure tbh.
        
    return capital_list
        

#sorting algorithm so we don't have to sort things everytime.
# get all of this to be object-oriented? I'm rewriting code a lot of the time for this one.  
    
    
#get information from a saved file somewhere: 
read_file = open(r"C:\Users\VSSip\Victor's Projects\Test.txt", 'r').read()#we need the .read() so that the open function knows that it needs to read the entire file. 
#read_file = ''

print(count_Words(read_file))
print(capital_letters(read_file))