import functools


def print_inventory(inv={}):
    msg = "Inventory:\n\n"
    msg += "\n".join([f'{key} {value}' for key, value in inv.items()])
    return msg


def add_to_inventory(inv={}, add=[]):
    updated_inventory = inv.copy()
    for item in add:
        updated_inventory.setdefault(item, 0)
        updated_inventory[item] += 1
    return updated_inventory
