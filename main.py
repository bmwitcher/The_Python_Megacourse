import functions

# from functions import get_todos, write_todos
''' calling the functions above from the functions.py file 
    only works when the two files are within the same directory 
    
    if you just import functions you have to specify the on the specific function 
    i.e. functions.get_todos()
'''

while True:
    ''' Designed to get user input and strip space chars from it '''
    user_action = input("Type add + todo item | show | edit # | complete # | erase # or exit to leave the program:  ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

        print(f"Item has been added to the list ")

    elif user_action.startswith("show"):  # use either option to print out results to screen

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # this line eliminates line 29-30
            item = item.title()
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            print(f" Here are the existing {todos}")

            new_todo = input("Enter a new todo item: ")
            todos[number] = new_todo + '\n'

            print(f"Here are the new {todos}".replace('\n', ''))

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue  # this will loop back to the top and request input

    elif user_action.startswith("erase"):
        try:
            number = int(user_action[6:])

            todos = functions.get_todos()
            print(f"{todos[number - 1]} has been removed from the list")
            todos.pop(number - 1)

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number in the list")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todos_to_remove = todos[index].strip('\n').upper()

            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo item {todos_to_remove} was removed from the list")
        except IndexError:
            print("There is no item with that number in the list")

    elif user_action.startswith("exit"):
        break
    else:
        print("Hey you have entered an unfamiliar command!")

print("Operation Complete")
