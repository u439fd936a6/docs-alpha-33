"""Scratch module."""

def flatten(xs):
    return [y for x in xs for y in x]

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

def most_common(xs):
    return max(set(xs), key=xs.count) if xs else None

if __name__ == "__main__":
    print(list(chunks(range(5), 9)))

# cleanup later
