import datetime

MENU_OPTIONS = {
    "List Tasks": list_tasks,
    "Add New Task": add_task,
    "Modify Task": modify_task,
    "Delete Task": delete_task,
}
UNDERLINE = "--------------------------------------------------"

# task list dictionary structure:
# {
#     timestamp: {
#         timestamp: "Task",
#         ...,
#         timestamp: "Task"
#     }
# }
# TEST DATA FOR DEBUGGING
# task_list = {
#     datetime.datetime.now().timestamp(): {
#         datetime.datetime.now().timestamp(): "Test Task 1",
#         (datetime.datetime.now().timestamp() + 5): "Test Task 2",
#         (datetime.datetime.now().timestamp() + 10): "Test Task 4",
#         (datetime.datetime.now().timestamp() + 15): "Test Task 3",
#         (datetime.datetime.now().timestamp() + 20): "Test Task 5",
#     },
#     (datetime.datetime.now().timestamp() + 100000000): {
#         datetime.datetime.now().timestamp(): "Test Task 6",
#         (datetime.datetime.now().timestamp() + 500): "Test Task 7",
#         (datetime.datetime.now().timestamp() + 1000): "Test Task 8",
#         (datetime.datetime.now().timestamp() + 15000): "Test Task 9",
#         (datetime.datetime.now().timestamp() + 20000): "Test Task 10",
#     }
# }

task_list = {}


def show_menu():
    print(UNDERLINE)
    print("Options:")
    for i, option in enumerate(list(MENU_OPTIONS.keys())):
        print(f"\t{i+1}: {option}")
    choice = input("What would you like to do?")

    # Route to correct function


def list_tasks():
    print(UNDERLINE)
    if len(task_list) > 0:
        for date_timestamp in task_list:
            tasklist_datetime = datetime.datetime.fromtimestamp(date_timestamp)
            print(
                f"{tasklist_datetime.strftime('%A')} {tasklist_datetime.strftime('%b')} {tasklist_datetime.strftime('%d')}, {tasklist_datetime.strftime('%Y')}:"
            )
            print(UNDERLINE)
            for task_timestamp in task_list[date_timestamp]:
                task_datetime = datetime.datetime.fromtimestamp(task_timestamp)
                print(
                    f"\t{task_datetime.strftime('%X')}:\t{task_list[date_timestamp][task_timestamp]}"
                )
            print(UNDERLINE)
    else:
        print("There are no tasks to list.")


def add_task():
    pass


def modify_task():
    pass


def delete_task():
    pass


def run_tracker_client():
    show_menu()


if __name__ == "__main__":
    run_tracker_client()
