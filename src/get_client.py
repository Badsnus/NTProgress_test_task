from src.client import Client
from src.exceptions import MissedClientName


def get_client(client_name: str, clients: dict[str, Client]) -> Client:
    if not client_name:
        raise MissedClientName

    if client_name not in clients:
        clients[client_name] = Client(name=client_name)

    return clients[client_name]
