from dataclasses import dataclass
from datetime import datetime

from tabulate import tabulate


@dataclass
class Operation:
    amount: float
    date: datetime
    description: str
    type: str


class Client:

    def __init__(self, name: str, balance: float = 0) -> None:
        self.__name: str = name
        self.__balance: float = balance
        self.__operations: list[Operation] = []

    @property
    def balance(self):
        return self.__balance

    def __add_operation(self, operation_name: str, amount: float,
                        description: str) -> None:
        self.__operations.append(Operation(
            amount=amount,
            description=description,
            date=datetime.now(),
            type=operation_name,
        ))

    @staticmethod
    def __format_amount(amount: float) -> str:
        return f'${amount}'

    def deposit(self, amount: float, description: str) -> None:
        self.__balance += amount
        self.__add_operation('deposit', amount, description)

    def withdraw(self, amount: float, description: str) -> None:
        self.__balance -= amount
        self.__add_operation('withdraw', amount, description)

    def show_bank_statement(self, since: datetime, till: datetime) -> str:

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
