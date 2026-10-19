stack = []
queue = []
while True:
    print("===== Stack & Queue Menu =====")
    print("1) Push")
    print("2) Pop")
    print("3) Peek")
    print("4) Switch")
    print("5) Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        value = input("Enter value to push: ")
        stack.append(value)
        print("Pushed:", value)
    elif choice == "2":
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print("Removed:", stack.pop())
    elif choice == "3":
        if len(stack) == 0:
            print("Stack is empty!")
        else:
            print("Top:", stack[-1])
    elif choice == "4":
        print("\n1) Stack")
        print("2) Queue")
        structure = input("Choose structure: ")
        if structure == "1":
            print("Switched to Stack.")
            while True:
                print("\n--- Stack Menu ---")
                print("1) Push  2) Pop  3) Peek  4) Switch  5) Exit")
                action = input("Enter choice: ")
                if action == "1":
                    value = input("Enter value: ")
                    stack.append(value)
                    print("Pushed:", value)
                elif action == "2":
                    if not stack:
                        print("Stack is empty!")
                    else:
                        print("Removed:", stack.pop())
                elif action == "3":
                    if not stack:
                        print("Stack is empty!")
                    else:
                        print("Top:", stack[-1])
                elif action == "4":
                    break
                elif action == "5":
                    print("Goodbye!")
                    exit()
                else:
                    print("Invalid choice!")
        elif structure == "2":
            print("Switched to Queue.")
            while True:
                print("\n--- Queue Menu ---")
                print("1) Enqueue  2) Dequeue  3) Peek  4) Switch  5) Exit")
                action = input("Enter choice: ")
                if action == "1":
                    value = input("Enter value: ")
                    queue.append(value)
                    print("Added:", value)
                elif action == "2":
                    if not queue:
                        print("Queue is empty!")
                    else:
                        print("Removed:", queue.pop(0))
                elif action == "3":
                    if not queue:
                        print("Queue is empty!")
                    else:
                        print("Front:", queue[0])
                elif action == "4":
                    break
                elif action == "5":
                    print("Goodbye!")
                    exit()
                else:
                    print("Invalid choice!")
        else:
            print("Invalid structure choice!")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")