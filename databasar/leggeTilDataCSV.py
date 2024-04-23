import csv
import random

# Definerer bruksområder for kvart språk - utvid gjerne
areas = {
    'Python': ['AI', 'Statistics', 'Web Development', 'Data Analysis', 'Machine Learning'],
    'JS': ['Web Development', 'Frontend', 'Backend', 'Mobile Apps'],
    'C': ['System Programming', 'Game Development', 'Embedded Systems'],
    'Go': ['System Programming', 'Web Development', 'Cloud Computing'],
    'Java': ['Web Development', 'Mobile Apps', 'Enterprise Software'],
    'Scratch': ['Education', 'Game Development'],
    'HTML': ['Web Development'],
    'Kotlin': ['Mobile Apps', 'Web Development'],
    'React': ['Web Development', 'Mobile Apps'],
    'TypeScript': ['Web Development', 'Frontend', 'Backend'],
}

# Les dei eksisterande data
with open('dev-old.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Legg til kolonna "area" som header-row
data[0].append('area')

# Legg til tilfeldige bruksområder til data
for i in range(1, len(data)):  # Hopp over header
    language = data[i][0]
    if language in areas:
        area = random.choice(areas[language])
    else:
        area = 'Unknown'
    data[i].append(area)

# Write the new data to a new CSV file
with open('dev_bruk.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)