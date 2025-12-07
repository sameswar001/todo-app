FILE_PATH = "todos.txt"
def get_todos(filepath=FILE_PATH):
    """ It read the text file  and
     retun the list of todo items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILE_PATH):
    """ It write the todos to the filepath """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions")
