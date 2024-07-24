from enum import Enum


class TypeOfAccount(Enum):
    LANDLORD = 'LANDLORD'
    RENTER = 'RENTER'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]
