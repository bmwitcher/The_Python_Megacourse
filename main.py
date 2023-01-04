def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    # Designed to get user input and strip space chars from it
    user_action = input("Type add + todo item | show | edit # | complete # | erase # or exit to leave the program:  ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = get_todos('todos.txt')

        todos.append(todo)

        # file = open('todos.txt', 'w') # if the absolute file path needs to be use please use the r"<path>" option inside the file ()
        # file.writelines(todos)
        # file.close()

        write_todos('todos.txt', todos)

        print(f"Item has been added to the list ")

    elif user_action.startswith("show"):  # use either option to print out results to screen

        todos = get_todos('todos.txt')

        # new_todos = []
        # for item in todos:
        #   new_item = item.strip('\n')
        #   new_todos.append(new_item)
        # print(todos)

        # this one line of code below  eliminates lines 23-27 from being needed
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')  # this line eliminates line 29-30
            item = item.title()
            print(f"{index + 1}-{item}")
    elif user_action.startswith("edit"):
        try:
            # number = int(input("Number of the todo to edit: "))
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos('todos.txt')
            print(f" Here are the existing {todos}")

            new_todo = input("Enter a new todo item: ")
            todos[number] = new_todo + '\n'

            print(f"Here are the new {todos}".replace('\n', ''))

            write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is not valid.")
            continue  # this will loop back to the top and request input

    elif user_action.startswith("erase"):
        try:
            number = int(user_action[6:])
            # number = int(input(" Number of the todo to remove/erase: "))

            todos = get_todos('todos.txt')
            print(f"{todos[number - 1]} has been removed from the list")
            todos.pop(number - 1)

            write_todos('todos.txt', todos)
        except IndexError:
            print("There is no item with that number in the list")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos('todos.txt')
            index = number - 1
            todos_to_remove = todos[index].strip('\n').upper()

            todos.pop(index)

            write_todos('todos.txt', todos)

            print(f"Todo item {todos_to_remove} was removed from the list")
        except IndexError:
            print("There is no item with that number in the list")

    elif user_action.startswith("exit"):
        break
    else:
        print("Hey you have entered an unfamiliar command!")

print("Operation Complete")
