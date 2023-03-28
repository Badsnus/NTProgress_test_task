from datetime import datetime

from tabulate import tabulate

from client import Operation


class BankStatementTable:

    def __init__(self, operations: list[Operation]) -> None:
        self.__operations = operations

    @staticmethod
    def __format_amount(amount: float) -> str:
        return f'${amount}'

    def get(self, since: datetime, till: datetime) -> str:

        total_withdraw = total_deposit = total_balance = 0

        col_names = [
            'Date', 'Description', 'Withdrawals', 'Deposits', 'Balance',
        ]
        data = [['', 'Previous balance', '', '', '$0.00']]
        for operation in self.__operations:
            if since > operation.date:
                continue

            if till < operation.date:
                break

            if operation.type == 'deposit':
                total_balance += operation.amount
                total_deposit += operation.amount
            else:
                total_balance -= operation.amount
                total_withdraw += operation.amount

            get_amount_for_operation = {
                'deposit': ('', self.__format_amount(operation.amount)),
                'withdraw': (self.__format_amount(operation.amount), ''),
            }
            data.append([
                operation.date,
                operation.description,
                *get_amount_for_operation[operation.type],
                self.__format_amount(total_balance),
            ])

        data.append([
            '',
            'Totals',
            *(
                self.__format_amount(amount) for amount in
                (total_withdraw, total_deposit, total_balance)
            ),
        ])
        return tabulate(data, headers=col_names, tablefmt="fancy_grid")
