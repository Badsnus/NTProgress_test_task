from src.client import Client
from src.loader import CommandsList
from src.statement_table import BankStatementTable
from src.validators import validate_amount, validate_date


def do_command(client: Client,
               command_name: str, args: dict[str]) -> None | str:
    if command_name == CommandsList.deposit:
        amount = validate_amount(args.pop('amount', None))
        client.do_deposit(amount, args.pop('description', ''))

        return 'Deposit operation was successful!'

    if command_name == CommandsList.withdraw:
        amount = validate_amount(args.pop('amount', None))
        client.do_withdraw(amount, args.pop('description', ''))
        return 'Withdrawal operation was successful!'

    kwargs = {
        key: validate_date(args.pop(key, '')) for key in ('since', 'till')
    }
    statement_table = BankStatementTable(client.operations)
    print(statement_table.get(**kwargs))
