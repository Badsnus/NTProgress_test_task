import re

import regex_patterns
import exceptions
from client import Client
from validators import validate_amount, validate_command_name


def convert_argument_to_float(argument: tuple[str]) -> tuple[str, float]:
    return argument[0], float(argument[1])


def parse_row_command(row_command: str) -> tuple[str, dict[str]]:
    command_name = re.search(
        regex_patterns.COMMAND_NAME_PATTERN, row_command,
    )
    if not command_name:
        raise exceptions.MissedCommandName

    command_name = str(command_name.group()).strip()

    command_args = dict(
        re.findall(regex_patterns.STRING_ARGUMENTS_PATTERN, row_command),
    )
    command_args.update(map(
        convert_argument_to_float,
        re.findall(regex_patterns.FLOAT_ARGUMENTS_PATTERN, row_command),
    ))
    return command_name, command_args


def get_client(args: dict[str]) -> Client:
    client_name = args.pop('client', None)
    if not client_name:
        raise exceptions.MissedClientName

    if client_name not in CLIENTS:
        CLIENTS[client_name] = Client(name=client_name)

    return CLIENTS[client_name]


def make_command(client: Client, command_name: str, args: dict[str]) -> None:
    if command_name == 'deposit':
        amount = validate_amount(args.pop('amount', None))
        client.deposit(amount, args.pop('description', ''))

        print('Deposit operation was successful!')
    elif command_name == 'withdraw':
        amount = validate_amount(args.pop('amount', None))
        client.withdraw(amount, args.pop('description', ''))

        print('Withdrawal operation was successful!')
    else:
        print(client.show_bank_statement(**args))


def main():
    print('Service started!')
    while True:
        try:
            command_name, args = parse_row_command(input('> ').strip())
            validate_command_name(command_name)
            client = get_client(args)
            make_command(client, command_name, args)
        except exceptions.MissedCommandName:
            print('No entered the command name.')
        except exceptions.UnknownCommand:
            print('Entered unknown command.')
        except exceptions.MissedClientName:
            print('Did not entered a client name.')
        except exceptions.DepositAmountShouldBeNumber:
            print('Amount must be a number.')
        except TypeError as ex:
            print(ex.args)


if __name__ == '__main__':
    CLIENTS = {}
    main()
