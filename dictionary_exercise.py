marks = {
    'Dumintru': 10,
    'Ion': 8,
    'Maria': 7
}

#print(marks)
#print(type(marks))

#print(marks['Dumintru'])
#print(marks['Maria'])

# Add element in dictionary
marks['Andrei'] = 9
#print(marks)

#for mark in marks:
#   print(mark)
#    print(marks[mark])


#for key, value in marks.items():
#    print(key, value)

marks['Ion']   = 10
marks['Maria'] = 10

print(marks)

if 'Ion' in marks:
    print('Cheia exista.')
else:
    print('Cheia nu exista.')