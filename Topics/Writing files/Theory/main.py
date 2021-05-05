#  You can experiment here, it won’t be checked

# planets = ['Mercury\n', 'Venus\n', 'Earth\n', 'Mars\n', 'Jupiter\n', 'Saturn\n', 'Uranus\n', 'Neptune\n']
# file = open('planets.txt', 'w', encoding='utf-8')
# file.writelines(planets)
# print(planets)
# file.close()

file = open('animals.txt', 'r')
file_1 = open('animals_new.txt', 'w')
for i in file.readlines():
    file_1.write(i.rstrip('\n') + ' ')
print(file_1)
file.close()
file_1.close()
