# Ein kjapp og enkel gjennomgang av nokre filhandteringsteknikkar i Python.
# https://www.w3schools.com/python/python_ref_file.asp
# Sjå også dokumentasjonen til Python:
# https://docs.python.org/3/library/io.html

dokument = open("fil.txt", "w")
dokument.write("Dette er linje 1\n")
dokument.write("Dette er linje 2\n")
dokument.write("Dette er linje 3\n")
dokument.write("Dette er linje 4\n")
dokument.close()

dokument = open("fil.txt", "r")
print("dokument.read():")
print(dokument.read())
dokument.close()

dokument = open("fil.txt", "r")
print("dokument.readline():")
print(dokument.readline())
dokument.close()

dokument = open("fil.txt", "r")
print("dokument.readlines([0,2]):")
print(dokument.readlines(1))
dokument.close()