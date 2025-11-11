import datetime

MENU_OPTIONS = ["List Tasks", "Add New Task", "Modify Task", "Delete Task"]

# task list dictionary structure:
# {
#     timestamp: {
#         timestamp: "Task",
#         ...,
#         timestamp: "Task"
#     }
# }
task_list = {}


def show_menu():
    print("What would you like to do?")

    for i, option in enumerate(MENU_OPTIONS):
        print(f"{i+1}: {option}")


def list_tasks():
    if len(task_list) > 0:
        for date_timestamp in task_list:
            tasklist_datetime = datetime.datetime.fromtimestamp(date_timestamp)
            print(
                f"{tasklist_datetime.strftime('%A')} {tasklist_datetime.strftime('%b')} {tasklist_datetime.strftime('%d')}, {tasklist_datetime.strftime('%Y')}:"
            )
            for task_timestamp in task_list[date_timestamp]:
                task_datetime = datetime.datetime.fromtimestamp(task_timestamp)
                print(
                    f"\t{task_datetime.strftime('%X')}:\t{task_list[date_timestamp][task_timestamp]}"
                )
    else:
        print("There are no tasks to list.")


def run_tracker_client():
    show_menu()


if __name__ == "__main__":
    run_tracker_client()
