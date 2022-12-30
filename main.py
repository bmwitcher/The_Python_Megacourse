
while True:
    # Designed to get user input and strip space chars from it
    user_action = input("Type add + todo item | show | edit and a number | complete and a number | erase and a number or exit to leave the program:  ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:] + '\n'

        with open('todos.txt','r') as file:
            todos = file.readlines()

        todos.append(todo)

        # file = open('todos.txt', 'w') # if the absolute file path needs to be use please use the r"<path>" option inside the file ()
        # file.writelines(todos)
        # file.close()

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)
        print(f"Item has been added to the list ")

    elif 'show' in user_action: # use either option to print out results to screen

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = []
        # for item in todos:
        #   new_item = item.strip('\n')
        #   new_todos.append(new_item)
        # print(todos)

        # this one line of code below  eliminates lines 23-27 from being needed
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n') # this line eliminates line 29-30
            item = item.title()
            print(f"{index + 1}-{item}")
    elif 'edit' in user_action:
        # number = int(input("Number of the todo to edit: "))
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        print(f" Here are the existing {todos}")

        new_todo = input("Enter a new todo item: ")
        todos[number] = new_todo + '\n'

        print(f"Here are the new {todos}".replace('\n',''))

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

    elif 'erase' in user_action:
        number = int(user_action[6:])
        # number = int(input(" Number of the todo to remove/erase: "))

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)
        print(f"{todos[number]} has been removed from the list")
        todos.pop(number - 1)

    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todos_to_remove = todos[index].strip().upper()

        todos.pop(index)

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

        print(f"Todo item {todos_to_remove} was removed from the list")

    elif 'exit' in user_action:
        break
    else:
        print("Hey you have entered an unfamiliar command!")

print("Operation Complete")

