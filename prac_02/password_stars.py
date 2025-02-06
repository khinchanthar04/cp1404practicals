PASSWORD_LENGTH = 10

def main():
    user_password = get_password()
    print_asterisks(user_password)


def print_asterisks(user_password):
    print("*" * user_password)


def get_password():
    user_password = len(input("Enter your password: "))
    while user_password <= PASSWORD_LENGTH:
        print("Invalid Password")
        user_password = len(input("Enter your password: "))
    return user_password


main()

