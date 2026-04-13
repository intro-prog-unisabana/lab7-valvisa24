import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    pass

def encrypt_single_pass(filename):
    f = open(filename, "r")
    password = f.read().strip()
    f.close()

    encrypted = caesar_encrypt(password)

    f = open(filename, "w")
    f.write(encrypted)
    f.close()


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    pass

def encrypt_passwords_in_file(filename):
    f = open(filename, "r")
    reader = csv.reader(f)
    rows = list(reader)
    f.close()

    for i in range(1, len(rows)):  # saltar encabezado
        if len(rows[i]) > 0:
            rows[i][2] = caesar_encrypt(rows[i][2])

    f = open(filename, "w", newline="")
    writer = csv.writer(f)
    writer.writerows(rows)
    f.close()


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass

def change_password(filename, website, password):
    f = open(filename, "r")
    reader = csv.reader(f)
    rows = list(reader)
    f.close()

    found = False

    for i in range(1, len(rows)):
        if rows[i][0] == website:
            rows[i][2] = caesar_encrypt(password)
            found = True

    if not found:
        return False

    f = open(filename, "w", newline="")
    writer = csv.writer(f)
    writer.writerows(rows)
    f.close()

    return True

def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass

def add_login(filename, website_name, username, password):
    encrypted = caesar_encrypt(password)

    f = open(filename, "a", newline="")
    writer = csv.writer(f)
    writer.writerow([website_name, username, encrypted])
    f.close()
