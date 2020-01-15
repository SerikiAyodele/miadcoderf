file=open("file.txt", "a")
file.write("\nthis is another line added from python")
file.write("\nanother line added")
file.close()

file=open("file.txt","r")
print(file.read())
file.close()
