from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime

from loader import OperationTypes


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
    def name(self):
        return self.__name

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def operations(self):
        return deepcopy(self.__operations)

    def __add_operation(self, operation_name: str, amount: float,
                        description: str) -> None:
        self.__operations.append(Operation(
            amount=amount,
            description=description,
            date=datetime.now(),
            type=operation_name,
        ))

    def do_deposit(self, amount: float, description: str) -> None:
        self.__balance += amount
        self.__add_operation(OperationTypes.deposit, amount, description)

    def do_withdraw(self, amount: float, description: str) -> None:
        self.__balance -= amount
        self.__add_operation(OperationTypes.withdraw, amount, description)
