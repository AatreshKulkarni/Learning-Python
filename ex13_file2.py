# File Operations : Opening file, Writing into the file

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that , hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opeing the file...")
# Opening a file with write permission
target = open(filename, 'w+')

print("Truncating the file. GOODBYE!")
# Deleting the file target
target.truncate()

print("Now I'm going to ask you for three lines.")

# Asking user input to write into the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")


print("I'm going to write these to the file.")

# Writing into the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print("And finally, we close it.")
# Closing the file
target.close()