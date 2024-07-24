from enum import Enum


class PropertyType(Enum):
    APARTMENT = 'APARTMENT'
    HOUSE = 'HOUSE'
    VILLA = 'VILLA'
    HOSTEL = 'HOSTEL'
    CAMPING = 'CAMPING'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]
