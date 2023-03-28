from client import Client
from exceptions import MissedClientName


def get_client(args: dict[str], clients: dict[Client]) -> Client:
    client_name = args.pop('client', None)
    if not client_name:
        raise MissedClientName

    if client_name not in clients:
        clients[client_name] = Client(name=client_name)

    return clients[client_name]
