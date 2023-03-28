class MissedCommandName(Exception):
    """No entered the command name."""


class MissedClientName(Exception):
    """Didnt entered a client name."""


class UnknownCommand(Exception):
    """Entered unknown command."""


class DepositAmountShouldBeNumber(Exception):
    """Amount must be a number."""


class InvalidDateFormat(Exception):
    """Entered invalid date format."""
