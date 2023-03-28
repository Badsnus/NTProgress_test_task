TABLE_PRINT_TYPE = 'fancy_grid'


class OperationTypes:
    deposit = 'deposit'
    withdraw = 'withdraw'


class CommandsList(OperationTypes):
    show_bank_statement = 'show_bank_statement'
    fields = [
        OperationTypes.deposit, OperationTypes.withdraw,
        show_bank_statement,
    ]
