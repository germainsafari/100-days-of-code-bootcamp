with open("C:/Users/safarig/Desktop/ger.txt") as file:
    contents = file.read()
    print(contents)

with open("new file", mode="w") as file:
    file.write("why are you not answering the call")
