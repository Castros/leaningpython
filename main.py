def get_todos():
    with open('files/todos.txt', 'r') as file:
         todos = file.readlines()
    return todos
  
         
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    # todo = input(user_prompt)

    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = get_todos()

        todos.append(todo + '\n')

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        todos = get_todos()
        
        for index, item in enumerate(todos):
            # item = item.title()
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        # we could use int or float if to convert string number to intNo obj
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
           
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
            
            user_action = input("Type add, show, edit, complete or exit:")
            user_action = user_action.strip()

    elif user_action.startswith("complete"):
        try: 
            number = int(user_action[9:])
            
            todos = get_todos()

            index = number - 1     
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."    
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
            
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye!")

