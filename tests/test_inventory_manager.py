from .context import exercises


def test_greet():
    assert exercises.inventory_manager.greet() == 'hello'
