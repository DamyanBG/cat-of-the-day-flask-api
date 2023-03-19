import enum


class RoleType(enum.Enum):
    uploader = "uploader"
    voter = "voter"
    admin = "admin"


# class State(enum.Enum):
#     pending = "pending"
#     accepted = "accepted"
#     rejected = "rejected"


# class Status(enum.Enum):
#     open = "open"
#     closed = "closed"


# class Shipped(enum.Enum):
#     yes = "yes"
#     no = "no"
