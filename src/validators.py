from datetime import datetime

import dateparser

from src.exceptions import (
    UnknownCommand,
    DepositAmountShouldBeNumber,
    InvalidDateFormat,
)
from src.loader import CommandsList


def validate_command_name(command_name: str) -> None:
    if command_name not in CommandsList.fields:
        raise UnknownCommand


def validate_amount(amount: str | None) -> float:
    try:
        if isinstance(amount, str) and 'inf' in amount:
            raise TypeError

        amount = float(amount)
    except (TypeError, ValueError):
        raise DepositAmountShouldBeNumber

    return amount


def validate_date(date: str) -> datetime:
    try:
        date = dateparser.parse(date)
    except TypeError:
        raise InvalidDateFormat

    if not date:
        raise InvalidDateFormat
    return date
