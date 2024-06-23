#!/usr/bin/env python3

import argparse

def check_password_complexity(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(c.isupper() for c in password)
    lowercase_criteria = any(c.islower() for c in password)
    digit_criteria = any(c.isdigit() for c in password)
    special_criteria = any(c in '!@#$%^&*()-_=+[{]};:\'",<.>/?' for c in password)
    complexity_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_criteria])
    if complexity_score < 3:
        return "\033[91mWeak\033[0m"
    elif complexity_score < 5:
        return "\033[93mMedium\033[0m"
    else:
        return "\033[92mStrong\033[0m"


def main():
    parser = argparse.ArgumentParser(description='Check the complexity of a password.')
    parser.add_argument('password', type=str, help='The password to check')
    
    args = parser.parse_args()
    password = args.password
    
    complexity = check_password_complexity(password)
    
    print(f"Password '{password}' complexity: {complexity}")

if __name__ == "__main__":
    main()