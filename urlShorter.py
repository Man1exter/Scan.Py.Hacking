import pyshorteners

url = input("Your URL link => ")

print(pyshorteners.Shortener().clickru.short(url))