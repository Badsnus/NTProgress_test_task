from exceptions import UnknownCommand, DepositAmountShouldBeNumber
from loader import COMMANDS


def validate_command_name(command_name: str) -> None:
    if command_name not in COMMANDS:
        raise UnknownCommand


def validate_amount(amount: str | None) -> float:
    try:
        amount = float(amount)
    except ValueError:
        raise DepositAmountShouldBeNumber

    return amount
