#  reads only by default
#  use 'with' to both open and close a file inside the function.
with open("./text_file.txt") as file:
  contents = file.read()
  print(contents)

# change open(mode=) to change how to interact with a file.
# This function over-writes the text file
with open("text_file.txt", mode="w") as file:
  file.write("Write this new line of text.")
  
# # change open(mode=a) to append a file
# #  If the file name does not already exist python will create it and write the data.
with open("new_file.txt", mode="a") as file:
  file.write("\nWrite this new new new line of text.")