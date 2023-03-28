import re

import regex_patterns
from exceptions import MissedCommandName


def convert_argument_to_int(argument: tuple[str]) -> tuple[str, int]:
    return argument[0], int(argument[1])


def parse_command(row_command: str) -> tuple[str, dict[str]]:
    command_name = re.search(
        regex_patterns.COMMAND_NAME_PATTERN, row_command,
    )
    if not command_name:
        raise MissedCommandName

    command_name = str(command_name.group())

    command_args = dict(
        re.findall(regex_patterns.STRING_ARGUMENTS_PATTERN, row_command),
    )
    command_args.update(map(
        convert_argument_to_int,
        re.findall(regex_patterns.INT_ARGUMENTS_PATTERN, row_command),
    ))
    return command_name, command_args


def main():
    print('Service started!')
    while True:
        row_command = input('> ').strip()
        print(parse_command(row_command))


if __name__ == '__main__':
    main()
