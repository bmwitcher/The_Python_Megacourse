def get_todos(filepath='todos.txt'):
    """ must pass filepath above so that you don't
     have to explicitly set it when calling the function
    """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
