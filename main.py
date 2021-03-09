from assignment import binary_search, questions

print("Question number 1 - 12")
while True:
    check = input("Do you want to enter question number(Y/N): ")
    if check.lower() == 'n':
        break
    else:
        try:
            option = int(input("Choose Question Number: "))
        except ValueError:
            print("Ouestion number must be an interger!!")
            continue
        try:
            print(f"\nQuestion number {option}: ")
            if option == 9:
                some_list = [1, 2, 3, 4, 5, 6, 7, 10]
                num = int(input("Enter number to search: "))
                index = binary_search(some_list, 0, len(some_list) - 1, num)
                if index != -1:
                    print("List = ", some_list)
                    print("The index of the number is: ", index)
                else:
                    print("List = ", some_list)
                    print("The number is not found")
            else:
                func = questions[option]
                func()
        except KeyError:
            print("Question number does not exist!!")
