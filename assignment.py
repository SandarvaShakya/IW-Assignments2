def paragraph():
    """
    1. Create a variable, paragraph, that has the following content:
    "Python is a great language!", said Fred. "I don't ever remember
    having this much fun before."
    """
    paragraph = """ 
        "Python is a great language!", said Fred.
        "I don't ever remember having this much fun before."
    """
    print(paragraph)


def is_leapyear():
    """
    2. Write an if statement to determine whether a variable holding a year is
    a leap year.
    """
    try:
        year = int(input("Enter year: "))
        if not year % 4:
            if not year % 100:
                if not year % 400:
                    print("It is leap year.")
                else:
                    print("It is not leap year.")
            else:
                print("It is leap year.")
        else:
            print("It is not a leap year.")
    except TypeError:
        print("Error: Enter integer!")


def is_anagram():
    """
    3. Write code that will print out the anagrams (words that use the same
    letters) from a paragraph of text.
    """
    list_of_words = ["cat", "god", "dog", "act", "car", "arc", "tree"]
    anagram = []
    for word_1 in list_of_words:
        for word_2 in list_of_words:
            if word_1 != word_2 and sorted(word_1) == sorted(word_2):
                anagram.append(word_1)

    print(f"Original list= {list_of_words}")
    print(f"Anagram = {anagram}")


def append_friends():
    """
    4. Create a list. Append the names of your colleagues and friends to it.
    Has the id of the list changed? Sort the list. What is the first item on
    the list? What is the second item on the list?
    """
    list_of_friends = []
    names = ["Ram", "Hari", "Sita"]
    for name in names:
        list_of_friends.append(name)

    list_of_friends.sort()
    print(f"Sorted, Appended list: {list_of_friends}")
    print("The id does not change.")
    index = 1
    for friend in list_of_friends:
        print(f"{index}. {friend}")
        index += 1


def list_of_tuple():
    """
    5. Create a tuple with your first name, last name, and age. Create a list,
    people, and append your tuple to it. Make more tuples with the
    corresponding information from your friends and append them to the
    list. Sort the list. When you learn about sort method, you can use the
    key parameter to sort by any field in the tuple, first name, last name,
    or age.
    """
    my_tuple = ("Sandarva", "Shakya", 19)
    friend_tuple = ("Lolem", "Polem", 19)
    tuple_list = []
    tuple_list.append(my_tuple)
    tuple_list.append(friend_tuple)
    print(f"Tuples = {my_tuple} {friend_tuple}")
    print(f"List = {tuple_list}")
    tuple_list.sort(key=lambda x: x[1])
    print(f"Sorted: {tuple_list}")


def find_john():
    """
    6. Create a list with the names of friends and colleagues. Search for the
    name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
    """
    friend_list = ["Harry", "Ron", "John", "Hermione"]
    for friend in friend_list:
        if friend.upper() == "JOHN":
            found = True
            break
        else:
            found = False
    print(friend_list)
    if found:
        print("Found!")
    else:
        print("Not Found!")


def average_age():
    """
    7. Create a list of tuples of first name, last name, and age for your
    friends and colleagues. If you don't know the age, put in None. Calculate
    the average age, skipping over any None values. Print out each name,
    followed by old or young if they are above or below the average age.
    """
    tuple_list = [
        ('Lolem', 'Polem', "19"),
        ('Sandarva', 'Shakya', "19"),
        ('Hermione', 'Granger', "17"),
        ('Harry', 'Potter', "None")]
    average = 0
    for tuple in tuple_list:
        if tuple[2].isdigit():
            average += int(tuple[2])
    average /= len(tuple_list)
    print(f"The average age is {average}")
    for tuple in tuple_list:
        if tuple[2].isdigit():
            if int(tuple[2]) < average:
                print(f"{tuple[0]} is young.")
            else:
                print(f"{tuple[0]} is old.")
        else:
            print(f"The age of {tuple[0]} is not known.")


def is_prime():
    """
    8. Write a function, is_prime, that takes an integer and returns True if
    the number is prime and False if the number is not prime.
    """
    num = int(input("Enter a number: "))
    count = 0
    for integer in range(1, num+1):
        if num % integer:
            count += 1
    if count <= 2:
        print("It is prime!")
    else:
        print("It is not prime!")


def binary_search(some_list, start, end, num):
    """
    9. Write a binary search function. It should take a sorted sequence and
    the item it is looking for. It should return the index of the item if
    found.It should return -1 if the item is not found.
    """
    if end >= start:
        mid_index = (end + start) // 2
        if some_list[mid_index] == num:
            return mid_index
        elif some_list[mid_index] > num:
            return binary_search(some_list, start, mid_index - 1, num)
        else:
            return binary_search(some_list, mid_index + 1, end, num)
    else:
        return -1


def convert():
    """
    10. Write a function that takes camel-cased strings (i.e.
    ThisIsCamelCased), and converts them to snake case (i.e.
    this_is_camel_cased). Modify the function by adding an argument,
    separator, so it will also convert to the kebab case
    (i.e.this-is-camel-case) as well.

    """
    some_string = "ThisIsCamelCase"
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print("String: ", some_string)
    snake = [some_string[0].lower(), ]
    kebab = [some_string[0].lower(), ]
    for character in some_string[1:]:
        if character in alphabets:
            snake.append('_')
            kebab.append('-')
            snake.append(character.lower())
            kebab.append(character.lower())
        else:
            snake.append(character)
            kebab.append(character)

    snake = "".join(snake)
    kebab = "".join(kebab)

    print("Snake case: ", snake)
    print("Kebab case: ", kebab)


def file():
    """
    11. Create a variable, filename. Assuming that it has a three-letter
    extension, and using slice operations, find the extension. For
    README.txt, the extension should be txt. Write code using slice
    operations that will give the name without the extension. Does your
    code work on filenames of arbitrary length?
    """
    file_name = "README.txt"

    print("Original file name: ", file_name)
    for char in file_name:
        if char == '.':
            file_name = file_name.split('.')
            break
    file_name = file_name[0]
    print("Without extension: ", file_name)


def is_palindrome():
    """
    12. Create a function, is_palindrome, to determine if a supplied word is
    the same if the letters are reversed.
    """
    word = "tat"
    print("Word: ", word)
    if list(reversed(word)) == list(word):
        print("It is palindrome.")
    else:
        print("It is not palindrome.")


questions = {
    1: paragraph,
    2: is_leapyear,
    3: is_anagram,
    4: append_friends,
    5: list_of_tuple,
    6: find_john,
    7: average_age,
    8: is_prime,
    10: convert,
    11: file,
    12: is_palindrome
}
