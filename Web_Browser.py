#imports
import webbrowser
import time

#code
print("---  Made by Harman  ---")
for i in range (100):
    time.sleep(1.5)
    search = input("What to search? ")
    webbrowser.open("https://www.google.com/search?q=" + search)
    print(" ")