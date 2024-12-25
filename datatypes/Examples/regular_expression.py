import re

text = "No one can play your role better than you"
pattern = r"than"


#search
#print("\\033[1mThis  is example for search in regualr expression\\033[0m")
search = re.search(pattern, text)
if search:
    print("Word found in sentence",search.group())
else:
    print("not found")

#match
#print("\\033[1mThis  is example for split in match expression\\033[0m")
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

#re.match() searches for matches from the beginning of a string. 
#re.search() searches for matches anywhere in the string.

# replace
#print("\\033[1mThis  is example for replace in regualr expression\\033[0m")
text = "I like black colour"
pattern = "black"
replace = "white"
new_text = re.sub(pattern, replace, text)
print(new_text)
#print("\\033[1mThis  is example for split in regualr expression!\\033[0m")


#split
numbers = "1,2,3,4"
pattern = ","
results = re.split(pattern, numbers)
print("print result in list formate",results)
print("print result in one by one")
for result in results:
    print(result)