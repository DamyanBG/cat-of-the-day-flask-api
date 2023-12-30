import enum


class RoleType(enum.Enum):
    uploader = "uploader"
    voter = "voter"
    admin = "admin"
    user = "user"
