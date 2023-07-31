#!/usr/bin/env python3

from pathlib import Path
import argparse

class UnauthorizedUserException(Exception):
    pass

def check_username(username: str, file_path: Path):
    with open(file_path, 'r') as file:
        authorized_users = file.read().splitlines()
        if username in authorized_users:
            return True
        else:
            raise UnauthorizedUserException(f"{username} is not authorized. ABORT!")

def main(username: str, file_path: Path):
    try:
        check_username(username, file_path)
        print(f"{username} is an authorized member.")
    except UnauthorizedUserException as e:
        print(e)
        raise PermissionError(f"{username} is not authorized to dispatch workflows!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate if a username exists in a file containing authorized users.")
    parser.add_argument("-g", "--github_id", type=str, help="Github ID of user to validate", required=True)
    parser.add_argument("-p", "--project", type=str, help="Name of the project to validate users", required=True)
    parser.add_argument("-d", "--dir_project", type=Path, help="Path to the directory containing project users", default='/', required=False)

    args = parser.parse_args()

    file_path = args.dir_project / args.project + '.txt'
    main(args.github_id, file_path)

