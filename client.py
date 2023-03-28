import dataclasses
from datetime import datetime

from tabulate import tabulate


@dataclasses.dataclass
class Operation:
    amount: float
    current_balance: float
    date: datetime
    description: str
    type: str


class Client:

    def __init__(self, name: str, balance: float = 0) -> None:
        self.__name: str = name
        self.__balance: float = balance
        self.__total_deposits: float = 0
        self.__total_withdraws: float = 0
        self.__operations: list[Operation] = []

    @property
    def balance(self):
        return self.__balance

    def __add_operation(self, operation_name: str, amount: float,
                        description: str) -> None:
        self.__operations.append(Operation(
            amount=amount,
            current_balance=self.balance,
            description=description,
            date=datetime.now(),
            type=operation_name,
        ))

    @staticmethod
    def __format_amount(amount: float) -> str:
        return f'${amount}'

    def deposit(self, amount: float, description: str) -> None:
        self.__balance += amount
        self.__total_deposits += amount
        self.__add_operation('deposit', amount, description)

    def withdraw(self, amount: float, description: str) -> None:
        self.__balance -= amount
        self.__total_withdraws += amount
        self.__add_operation('withdraw', amount, description)

    def show_bank_statement(self, since: datetime, till: datetime) -> str:
        col_names = [
            'Date', 'Description', 'Withdrawals', 'Deposits', 'Balance',
        ]
        data = [['', 'Previous balance', '', '', '$0.00']]
        for operation in self.__operations:
            if since > operation.date:
                continue

            if till < operation.date:
                break

            get_amount_for_operation = {
                'deposit': ('', self.__format_amount(operation.amount)),
                'withdraw': (self.__format_amount(operation.amount), ''),
            }
            data.append([
                operation.date,
                operation.description,
                *get_amount_for_operation[operation.type],
                self.__format_amount(operation.current_balance),
            ])

        data.append([
            '',
            'Totals',
            *(
                self.__format_amount(amount) for amount in
                (self.__total_withdraws, self.__total_deposits, self.balance)
            ),
        ])
        return tabulate(data, headers=col_names, tablefmt="fancy_grid")


c = Client('asd')
c.deposit(100.0, 'dep')
c.withdraw(50, 'withdraw')
print(c.show_bank_statement(datetime(2020, 10, 23, 1),
                            datetime(2025, 10, 23, 1)))
