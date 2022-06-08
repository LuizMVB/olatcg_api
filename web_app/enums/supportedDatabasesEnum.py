from enum import Enum

class SupportedDatabasesEnum(Enum):
    DEFAULT = "OLATCGDB"
    NCBI_NT = "NCBI_NT"

    def __str__(self):
        return self.value