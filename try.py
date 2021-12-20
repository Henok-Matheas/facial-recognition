file = open(r"people.txt","a")
file.write("Henok ")
file.write("dibaba ")
file.close()


reading = open(r"people.txt","r")
names = reading.read()
name_list = names.split()
print(name_list)
reading.close()