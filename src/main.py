from classes.password import Password


def main():

    my_password = Password()

    my_password.create_random_password()
    print(my_password.password)


if __name__ == "__main__":
    main()
