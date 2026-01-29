from src.constants import DataTypes


def infer_value(value: str) -> DataTypes:
    # TODO needs work
    return DataTypes.FLOAT


def is_int(value: str) -> bool:
    return value.isdecimal()


def is_float(value: str) -> bool:
    if not value:
        return False
    if value == ".":
        return False

    mp = {str(i): -1 for i in range(10)}
    mp["."] = 1
    for c in value:
        if not mp.get(c):
            return False
        mp[c] = mp.get(c) - 1

    return True
