words = """
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
"""
print(words)
wordlist = words.split(sep=" ")
print(wordlist)
my_dict = dict.fromkeys(wordlist)
print(my_dict)
for word in wordlist:
    if my_dict[word] is None:
        my_dict[word] = 1
    else:
        my_dict[word] += 1
print(my_dict)
l = list(my_dict.items())
print(l)
l.sort(key=lambda x: x[1], reverse=True)
print(l)
maxlist = l[:5]
print(maxlist)
