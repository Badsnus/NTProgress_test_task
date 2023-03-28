import re

import exceptions
import regex_patterns


class RowCommandParser:

    def __init__(self, row_command: str) -> None:
        self.row_command = row_command.strip()

    @staticmethod
    def convert_argument_to_float(argument: tuple[str]) -> tuple[str, float]:
        return argument[0], float(argument[1])

    def parse_row_command(self) -> tuple[str, dict[str]]:
        command_name = re.search(
            regex_patterns.COMMAND_NAME_PATTERN, self.row_command,
        )
        if not command_name:
            raise exceptions.MissedCommandName

        command_name = str(command_name.group()).strip()

        command_args = dict(
            re.findall(
                regex_patterns.STRING_ARGUMENTS_PATTERN,
                self.row_command,
            ),
        )
        command_args.update(map(
            self.convert_argument_to_float,
            re.findall(
                regex_patterns.FLOAT_ARGUMENTS_PATTERN,
                self.row_command,
            ),
        ))
        return command_name, command_args
