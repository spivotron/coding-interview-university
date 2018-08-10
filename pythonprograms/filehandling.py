# Create a new file
my_file = open("test1.txt", 'w')
my_file.write("This is a test line\n")
# my_file.close()

# Read the file
my_file = open("test1.txt", 'r')
# print(my_file.read())


# add a new line and read
my_file = open("test1.txt", 'a')
my_file.write("this is a second line\n")
# my_file.close()

my_file = open("test1.txt", "r")
# print(my_file.read())

# Reading a file with readlines, which has a separator
my_file = open("test1.txt", "a")
my_file.write("this is a third line\n")
my_file.close()

my_file = open("test1.txt", 'r')

print(my_file.readline()) # readline only reads the first line in the file
print(my_file.readlines(0))
my_file.close()

my_file = open("test2.txt", 'w')
my_file.write("First line \n")
my_file.write("Second line \n")
my_file.close()

for line in open("test2.txt"):print(line)



