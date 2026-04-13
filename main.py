from password_manager import add_login, change_password, encrypt_passwords_in_file

def main() -> None:
    filename = input("Enter the CSV file name:\n")

    # encriptar todas las contraseñas
    encrypt_passwords_in_file(filename)

    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        choice = input()

        # 🔹 OPCIÓN 1
        if choice == "1":
            data = input("Enter the website and the new password:\n").split()

            if len(data) < 2:
                print("Input is in the wrong format!")
                continue

            website, password = data

            if len(password) < 12:
                print("Password is too short!")
                continue

            success = change_password(filename, website, password)

            if not success:
                print("Website not found! Operation failed.")
            else:
                print("Password changed.")

        # 🔹 OPCIÓN 2
        elif choice == "2":
            data = input("Enter the website, username, and password:\n").split()

            if len(data) < 3:
                print("Input is in the wrong format!")
                continue

            website, username, password = data

            if len(password) < 12:
                print("Password is too short!")
                continue

            add_login(filename, website, username, password)
            print("Login added.")

        # 🔹 OPCIÓN 3
        elif choice == "3":
            break

        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()
