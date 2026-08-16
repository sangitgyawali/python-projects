# Writing to a file

with open("output.txt", "w") as file:
    file.write("hello, this is a sample text.")

# Reading from a file
with open("output.txt", "r") as file:
    data = file.read()
    print("Data from file:", data)