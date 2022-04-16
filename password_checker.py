import sys
import re
from string import punctuation
from password_requirements import password_requirements as pr


def password_checker(*args: str) -> list:
    """
    Takes password from CLI-command and checks it for certain requirements.
    :return: <List> unfulfilled_requirements_list containing unfulfilled requirements.
    """
    unfulfilled_requirements_list = []

    try:
        if args == ():
            password = sys.argv[1]
        else:
            password = args[0]

        password.encode("ascii")

        if re.search("[a-z]", password) is None \
                or re.search("[A-Z]", password) is None:
            unfulfilled_requirements_list.append(pr["upper_lower_chars"])

        if re.search("[0-9]", password) is None:
            unfulfilled_requirements_list.append(pr["digits"])

        if re.search("[" + punctuation + "]", password) is None:
            unfulfilled_requirements_list.append(pr["punctuation"])

        if not 14 <= len(password) <= 64:
            unfulfilled_requirements_list.append(pr["length"])

        return unfulfilled_requirements_list

    except IndexError:
        print("Please, provide a password in CLI-command as \"python password_checker.py {!password}\".")
    except UnicodeEncodeError:
        if __name__ == "__main__":
            print("Only ASCII, digit and punctuation symbols are allowed!")


if __name__ == "__main__":
    result = password_checker()

    if result is not None:
        if len(result) > 0:
            """
            Prints if password is weak or strong.
            If password is weak, gives statements for improvements.
            """
            print("Weak password:")
            print(*result, sep='\n')
        else:
            print("Strong password")
