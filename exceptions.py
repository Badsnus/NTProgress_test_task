class MissedCommandName(Exception):
    def __init__(self, message='U need to enter the command name', *args):
        super().__init__(message, *args)
