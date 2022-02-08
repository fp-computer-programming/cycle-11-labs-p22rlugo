# Ryan Lugo: RJL 2/8/22

my_file = open("alma_mater.txt", "r")

while True:
    line = my_file.readline()

    print(line[::-1],end= "")