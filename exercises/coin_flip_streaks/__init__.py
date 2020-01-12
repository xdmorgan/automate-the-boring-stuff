import random


def generate_string(len=10):
    turns = [random.choice(['H', 'T']) for i in range(len)]
    return " ".join(turns)


def streaks_in_string(s, streak_length=5):
    count = 0
    items = s.split()
    stack = []
    while len(items):
        head, *tail = items
        if len(stack) == 0 or head == stack[-1]:
            stack.append(head)
            if len(stack) == streak_length:
                count += 1
                stack = []
        else:
            stack = [head]
        items = tail
    return count


if __name__ == "__main__":
    cycles = 1000
    length = 1000
    results = []
    for _ in range(cycles):
        string = generate_string(length)
        assert len(string) == length + (length - 1)
        results.append(streaks_in_string(string, 6))
    assert len(results) == cycles
    avg = sum(results) / cycles
    print('average number of streaks', avg)
