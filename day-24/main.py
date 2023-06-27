# file = open('my_file.txt')

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
# file.close()

# with open("my_file.txt", 'r+') as file:
#     file.write("N text.")
    # contents = file.read()
    # print(contents)

with open("new_file.txt", 'w') as file:
    file.write("New text.")