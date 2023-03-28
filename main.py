import exceptions

from command_parser import RowCommandParser
from do_command import do_command
from get_client import get_client
from validators import validate_command_name


def main():
    print('Service started!')

    clients = {}

    while True:
        try:
            parser = RowCommandParser(input('> '))

            command_name, args = parser.parse_row_command()
            validate_command_name(command_name)
            client = get_client(args, clients)
            do_command(client, command_name, args)

        except exceptions.MissedCommandName as ex:
            print(ex.__doc__)
        except exceptions.UnknownCommand as ex:
            print(ex.__doc__)
        except exceptions.MissedClientName as ex:
            print(ex.__doc__)
        except exceptions.DepositAmountShouldBeNumber as ex:
            print(ex.__doc__)
        except exceptions.InvalidDateFormat as ex:
            print(ex.__doc__)
        except KeyboardInterrupt:
            print('Game over')
            break


if __name__ == '__main__':
    main()
