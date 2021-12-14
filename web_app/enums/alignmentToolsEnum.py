from enum import Enum

class AlignmentToolsEnum(Enum):
    NEEDLEMAN_WUNSCH = "Needleman-Wunsch"
    SMITH_WATERMAN = "Smith-Waterman"
    STRIPED_SMITH_WATERMAN = "Striped Smith Waterman"