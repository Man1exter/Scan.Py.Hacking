import wikipedia


what_to = input("your search from wikipedia => ")
search = wikipedia.summary(what_to,sentences=2)
print(search)