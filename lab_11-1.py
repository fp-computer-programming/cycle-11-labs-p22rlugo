# Ryan Lugo: 2/8/22

my_file = open("alma_mater.txt", "r")

while True:
    line = my_file.readline()
    print(line, end="")