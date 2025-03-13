from dataclasses import dataclass


@dataclass
class User:
    id: str
    username: str
    email: str
    password_hash: str