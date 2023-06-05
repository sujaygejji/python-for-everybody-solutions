String Parsing : Parsing a string means, to breakdown string into smaller components (substring), and extract this required substring.

Procedure;
First to determine start index (start point)  and end index. 
Then,  extract the substring between start index and end index using slicing method 

Here our aim is to extract the 0.8475 from the string.
#first store the entire string in some variable called str
str= “X-DSPAM-Confidence :0.8475 "
        
#find the starting index using find function. (here starting point is colon (:))
start = str.find(‘:’)    
                                          
#find the end index using find function. (here end index is white space(‘ ‘))
end = str.find(‘  ’, start)    
       or
# find the end index by finding total length of the string
end = len(str)    

# Now to extract the string between start point and end point
sub_string= str[start+1 : end]

# to convert this sub string into floating 
Number = float(sub_string)
print(Number)
