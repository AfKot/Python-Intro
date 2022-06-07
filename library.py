#CREATE DICTIONARY
book_case = {"JKR" : ["HP1", "HP2", "HP3", "HP4", "HP5", "HP6", "HP7"], "ROB MUCH" : ["Class A", "Maximum Security", "The Killing"], "RD" : ["BFG"]}

print("List of all the books in our library")
print(list(book_case.values()))

#ASK FOR INPUT
author = input("Please choose an author: ")
author_search = author.upper()
book_case[author_search].sort()

#JOINING EVERYTHING FIRST
output = ", ".join(book_case[author_search])
print(output)
