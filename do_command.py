from client import Client
from loader import CommandsList
from statement_table import BankStatementTable
from validators import validate_amount, validate_date


def do_command(client: Client, command_name: str, args: dict[str]) -> None:
    if command_name == CommandsList.deposit:
        amount = validate_amount(args.pop('amount', None))
        client.do_deposit(amount, args.pop('description', ''))

        print('Deposit operation was successful!')
    elif command_name == CommandsList.withdraw:
        amount = validate_amount(args.pop('amount', None))
        client.do_withdraw(amount, args.pop('description', ''))
        print('Withdrawal operation was successful!')
    else:
        kwargs = {
            key: validate_date(args.pop(key, '')) for key in ('since', 'till')
        }
        statement_table = BankStatementTable(client.operations)
        print(statement_table.get(**kwargs))
