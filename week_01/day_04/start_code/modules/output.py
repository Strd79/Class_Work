def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

def print_list(list):
    for task in list:
        print_task(task)

def mark_task_complete(task):
    task["completed"] = True

# add a task to the list
def add_to_list(list, task):
    list.append(task)

# create a menu
def print_menu():
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("Q or q: Quit")