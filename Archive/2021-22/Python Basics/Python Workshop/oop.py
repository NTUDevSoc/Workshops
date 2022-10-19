class Objects(object):
    def __init__(self, objectLookingAt, bookObjects):
        self.objectLookingAt = objectLookingAt
        self.bookObjects = bookObjects
        self.objects = ["book", "chair", "table", "window", "door"]

    def check_object_valid(self):
        if self.objectLookingAt in self.objects:
            return True
        else:
            return False
    
    def select_look_at_object(self):
        if self.objectLookingAt == "vase":
            print("You are looking at a vase")
        elif self.objectLookingAt == "book":
            self.book()
        elif self.objectLookingAt == "chair":
            self.chair()
        else:
            print("You can't see anything")


def main():
    objects_looked_at = []
    print("Welcome to the Escape Room")
    loop = True
    while loop:
        print("""
        1. Look at object
        2. Save stuff
        3. Load stuff
        4. Quit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            ans = input("Do you want to inspect the vase?")
            if ans == "yes":
                objects = Objects("vase", ["picture of cat", "some hash"])
                objects.select_look_at_object()
        elif choice == "4":
            print("Quitting")
            loop = False
        else:
            print("Invalid choice")
    print("Goodbye")

if __name__ == "__main__":
    main()