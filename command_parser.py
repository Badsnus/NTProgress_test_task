import re

from exceptions import MissedCommandName
from regex_patterns import (
    COMMAND_NAME_PATTERN,
    FLOAT_ARGUMENTS_PATTERN,
    STRING_ARGUMENTS_PATTERN,
)


class RowCommandParser:

    def __init__(self, row_command: str) -> None:
        self.row_command = row_command.strip()

    @staticmethod
    def convert_argument_to_float(argument: tuple[str]) -> tuple[str, float]:
        return argument[0], float(argument[1])

    def parse_row_command(self) -> tuple[str, dict[str]]:
        command_name = re.search(COMMAND_NAME_PATTERN, self.row_command)

        if not command_name:
            raise MissedCommandName

        command_name = str(command_name.group()).strip()

        command_args = dict(
            re.findall(STRING_ARGUMENTS_PATTERN, self.row_command),
        )
        command_args.update(map(
            self.convert_argument_to_float,
            re.findall(FLOAT_ARGUMENTS_PATTERN, self.row_command),
        ))
        return command_name, command_args
