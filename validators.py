from datetime import datetime

import dateparser

from exceptions import (
    UnknownCommand,
    DepositAmountShouldBeNumber,
    InvalidDateFormat,
)
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


def validate_date(date: str) -> datetime:
    date = dateparser.parse(date)

    if not date:
        raise InvalidDateFormat
    return date
