class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        pass

    def remove_task(self, task):
        pass

    def display_tasks(self):
        pass

def main():

    while True:
        print("\nSelect an option:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            '''......................'''
        elif choice == "2":
            task = input("Enter the task to remove: ")
            '''......................'''
        elif choice == "3":
            '''......................'''
        elif choice == "4":
            '''......................'''
            break
        else:
            '''......................'''

if __name__ == "__main__":
    main()
