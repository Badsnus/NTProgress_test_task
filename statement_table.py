from datetime import datetime

from tabulate import tabulate

from client import Operation
from loader import OperationTypes, TABLE_PRINT_TYPE


class BankStatementTable:

    def __init__(self, operations: list[Operation]) -> None:
        self.__operations = operations
        self.__total_balance = 0
        self.__total_deposit = 0
        self.__total_withdraw = 0

    @staticmethod
    def __format_amount(amount: float) -> str:
        return f'${amount}'

    def __get_operation_line(self, operation: Operation) -> list[str]:
        if operation.type == OperationTypes.deposit:
            self.__total_balance += operation.amount
            self.__total_deposit += operation.amount
        else:
            self.__total_balance -= operation.amount
            self.__total_withdraw += operation.amount

        get_amount_for_operation = {
            'deposit': ('', self.__format_amount(operation.amount)),
            'withdraw': (self.__format_amount(operation.amount), ''),
        }
        return [
            operation.date,
            operation.description,
            *get_amount_for_operation[operation.type],
            self.__format_amount(self.__total_balance),
        ]

    def __get_total_line(self):
        total = map(
            self.__format_amount,
            (
                self.__total_withdraw,
                self.__total_deposit,
                self.__total_balance,
            ),
        )

        return [
            '', 'Totals',
            *total,
        ]

    def get(self, since: datetime, till: datetime) -> str:
        col_names = [
            'Date', 'Description', 'Withdrawals', 'Deposits', 'Balance',
        ]
        data = [['', 'Previous balance', '', '', '$0.00']]

        for operation in self.__operations:
            if since > operation.date:
                continue

            if till < operation.date:
                break

            data.append(self.__get_operation_line(operation))

        data.append(self.__get_total_line())
        return tabulate(data, headers=col_names, tablefmt=TABLE_PRINT_TYPE)
