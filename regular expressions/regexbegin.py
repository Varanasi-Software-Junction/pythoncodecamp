"""
Python pckage for regex is  re
https://docs.python.org/3/library/re.html
import it like this
import re
Performing Matches
Once you have an object representing a compiled regular expression, what do you do with it? Pattern objects have several methods and attributes. Only the most significant ones will be covered here; consult the re docs for a complete listing.

Method/Attribute    Purpose

match()             Determine if the RE matches at the beginning of the string.

search()            Scan through a string, looking for any location where this RE matches.

findall()           Find all substrings where the RE matches, and returns them as a list.

finditer()          Find all substrings where the RE matches, and returns them as an iterator.



"""
import re
pattern = re.compile('[a-z]+')
s1="This is train no 4356 to Varanasi"
s2="this is "
print(pattern.match(s1))#Matches the whole string and returns a match object if found from the beginning or None
print(pattern.match(s2))
print(pattern.match(s1,re.IGNORECASE))#Matches the whole string and returns a match object if found from the beginning or None
#Using the matched object
m=pattern.match(s2)
print(m)
print("Starts from ", m.span()[0]," ends at ",m.span()[1])
print("The matched string", m[0])



