# Capgemini Engineering Python Internship Test


## Task 1: Password checker
Write a simple python console program that validates a password passed by the user as a
command-line argument against a set of rules:
1. The password contains both lowercase and uppercase characters
2. The password contains at least one digit
3. The password contains at least one punctuation character
4. The password is at least 14 characters long
The checker must print relevant error messages into the console in case of any violations.
Otherwise, the script must print “Strong password” into the console if all tests are passed.

Usage examples:  
All checks failed
```bash
-> internship python password_checker.py qwerty
Weak password:
- Password must contain both lowercase and uppercase characters
- Password must contain digits
- Password must contain at least one punctuation character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
- Password must be at least 14 (up to 64) characters long
```
Some checks passed
```bash
-> internship python password_checker.py Qwerty123
Weak password:
- Password must contain at least one punctuation character (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
- Password must be at least 14 (up to 64) characters long
```
All checks passed
```bash
-> internship python password_checker.py "The quick br0wn fox jumps 0ver the lazy d0g."
Strong password
```

## Task 2: Strong password generator
Write a simple python console program that generates a strong random password. A strong
password must pass all checks from the previous task i.e.:
• Contains both lowercase and uppercase characters
• Contains at least one digit
• Contains at least one punctuation character (see
https://docs.python.org/3/library/string.html#string.punctuation)
• Is at least 14 characters long.
    
  
Usage examples:  
The program generates a new password on each run
```bash
-> internship python strong_password_generator.py
%#$vL!Gz6o9M8L
-> internship python strong_password_generator.py
b4hD!vJ7%dWYVi
```
