import logging

import exceptions
from command_parser import RowCommandParser
from do_command import do_command
from get_client import get_client
from validators import validate_command_name


def main():
    logging.info('Service started!')
    clients = {}

    while True:
        try:
            parser = RowCommandParser(input('> '))

            command_name, args = parser.parse_row_command()
            validate_command_name(command_name)
            client = get_client(args, clients)

            if info := do_command(client, command_name, args):
                logging.info(info)

        except exceptions.MissedCommandName as ex:
            logging.error(ex.__doc__)
        except exceptions.UnknownCommand as ex:
            logging.error(ex.__doc__)
        except exceptions.MissedClientName as ex:
            logging.error(ex.__doc__)
        except exceptions.DepositAmountShouldBeNumber as ex:
            logging.error(ex.__doc__)
        except exceptions.InvalidDateFormat as ex:
            logging.error(ex.__doc__)
        except KeyboardInterrupt:
            logging.info('Game over')
            break


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S',
    )
    main()
