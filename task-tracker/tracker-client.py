MENU_OPTIONS = ["List Tasks", "Add New Task", "Modify Task", "Delete Task"]


def show_menu():
    print("What would you like to do?")

    for i, OPTION in enumerate(MENU_OPTIONS):
        print(f"{i+1}: {OPTION}")


def run_tracker_client():
    show_menu()


if __name__ == "__main__":
    run_tracker_client()
