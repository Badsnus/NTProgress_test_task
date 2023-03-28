import datetime

import pytest

import loader
from client import Client, Operation, OperationTypes
from command_parser import RowCommandParser
from exceptions import (
    DepositAmountShouldBeNumber,
    InvalidDateFormat,
    MissedClientName,
    MissedCommandName,
    UnknownCommand,
)
from get_client import get_client
from validators import (
    validate_amount,
    validate_command_name,
    validate_date,
)
from statement_table import BankStatementTable


class TestRowCommandParser:

    def test_missed_command_name(self):
        for arg in '', ' ', 'asd', 'asd ':
            with pytest.raises(MissedCommandName):
                RowCommandParser(arg).parse_row_command()

    def test_with_good_param(self):
        test_cases = [
            (
                'deposit --amount=100 --description="asd"',
                ('deposit', {'amount': 100, 'description': 'asd'}),
            ),
            (
                'withdraw --amount=123.53',
                ('withdraw', {'amount': 123.53}),
            ),
            (
                'gg --amount="123.53" --gg=1241414',
                ('gg', {'amount': '123.53', 'gg': 1241414}),
            ),  # был бы прод офк надо больше тестов.
        ]
        for row_command, result in test_cases:
            parser = RowCommandParser(row_command)
            assert result == parser.parse_row_command()


class TestValidateCommand:
    def test_unknown_command(self):
        for arg in 'gg wer', 'shit_name --amount=32':
            with pytest.raises(UnknownCommand):
                validate_command_name(arg)

    def test_good_commands(self):
        for arg in loader.CommandsList.fields:
            validate_command_name(arg)


class TestAmountValidator:
    def test_bad(self):
        for arg in 'hh', None, '576er', 'inf', '124.5435.234':
            with pytest.raises(DepositAmountShouldBeNumber):
                validate_amount(arg)

    def test_good(self):
        for arg in 1, 32, -100, 43, 23.5, '1241.634', '34234.5435':
            validate_amount(arg)


class TestDataValidator:

    def test_bad(self):
        for arg in None, '36-45654654642-4234', '2053-66-44':
            with pytest.raises(InvalidDateFormat):
                validate_date(arg)

    def test_good(self):
        for arg in '2023-03-28', '2053 12 23', '2021-01-02 12:30:00':
            validate_date(arg)


class TestGetClient:
    def test_no_client_in_args(self):
        with pytest.raises(MissedClientName):
            get_client({'gg': 'gg'}, {})

    def test_client(self):
        a = 'Some_name'
        clients = {}
        client = get_client({'client': a}, clients)
        assert isinstance(client, Client)
        assert client.name in clients
        assert client.name == a
        assert client.balance == 0

        assert get_client({'client': a}, clients) == client


class TestStatementTable:

    def test_table(self):
        assert isinstance(
            BankStatementTable([]).get(
                datetime.datetime.now(),
                datetime.datetime.now(),
            ), str)


class TestClient:

    def test_create_client(self):
        name = 'some_name'
        client = Client(name)
        assert client.name == name
        assert client.balance == 0
        assert client.operations == []

    def test_create_deposit(self):
        client = Client('some_name')
        amount = 123
        description = 'test-desc'
        client.do_deposit(amount, description)
        assert client.balance == amount
        assert len(client.operations) == 1
        operation = client.operations[0]
        assert isinstance(operation, Operation)
        assert operation.amount == amount
        assert operation.description == description
        assert operation.type == OperationTypes.deposit

    def test_create_withdraw(self):
        client = Client('some_name')
        amount = 123
        description = 'test-desc'
        client.do_withdraw(amount, description)
        assert client.balance == -amount
        assert len(client.operations) == 1
        operation = client.operations[0]
        assert isinstance(operation, Operation)
        assert operation.amount == amount
        assert operation.description == description
        assert operation.type == OperationTypes.withdraw

    def test_do_many_operations(self):
        client = Client('some_name')
        amount = 123
        for _ in range(4):
            client.do_deposit(amount, '')
        for _ in range(2):
            client.do_withdraw(amount, '')
        assert client.balance == amount * 2
        assert len(client.operations) == 6
