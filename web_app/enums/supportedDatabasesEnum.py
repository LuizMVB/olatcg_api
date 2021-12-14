from enum import Enum

class SupportedDatabasesEnum(Enum):
    DEFAULT = "OLATCGDB"

    def __str__(self):
        return self.value