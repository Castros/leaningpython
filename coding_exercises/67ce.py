
# file = open('coding_exercises/essay.txt', 'r')
# readfile = file.read()
# print(readfile.title())

# mycode
# file = open('coding_exercises/essay.txt', 'r')
# readfile = file.read()

# print(len(readfile.title()))

# teacherscode
# file = open("essay.txt", 'r')
# content = file.read()

# nr_chars = len(content)
# print(nr_chars)

# todo = input("Add a new memeber: ") + "\n"

# file = open('coding_exercises/members.txt', 'r')
# todos = file.readlines()
# file.close()
# todos.append(todo)           
# file_write = open('coding_exercises/memebers.txt', 'w')
# file_write.writelines(todos)
# file_write.close()

# print(todos)

#this will create a text 
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for filename in filenames:
#     file = open(filename, 'w')
#     file.write("Hello")
#     file.close()

filenames = ['files/a.txt', 'files/b.txt', 'files/c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read()
    print(content)