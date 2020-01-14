from .context import exercises

INVENTORY = {'Sword': 420, 'Shield': 69, 'something': 123}
PRINTED_INVENTORY = """Inventory:

Sword 420
Shield 69
something 123"""

ADD_TO_INVENTORY = ['Sword', 'Shield', 'Shield', 'cat', 'Shield', 'cat']
UPDATED_INVENTORY = {'Sword': 421, 'Shield': 72, 'something': 123, 'cat': 2}


def test_print_inventory():
    assert exercises.inventory_manager.print_inventory(
        INVENTORY) == PRINTED_INVENTORY


def test_add_to_inventory():
    assert exercises.inventory_manager.add_to_inventory(
        INVENTORY, ADD_TO_INVENTORY) == UPDATED_INVENTORY
