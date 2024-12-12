def reverse_string(input_string):
    """
    Функція, яка приймає рядок і повертає його "віддзеркалений" варіант.
    """
    return input_string[::-1]


if __name__ == "__main__":
    user_input = input("Введіть рядок для інвертування: ")
    print("Інвертований рядок:", reverse_string(user_input))
