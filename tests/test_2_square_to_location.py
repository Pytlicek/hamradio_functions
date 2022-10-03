from src.qth_locator import square_to_location


def test_square_to_location_positive():
    squares = [
        ("KM32", None),
        (None, None),
        ("KM32jn", (32.541667, 26.75)),
        ("KM72kk", (32.416667, 34.833333)),
        ("JN45fo", (45.583333, 8.416667)),
        ("KO92so", (52.583333, 39.5)),
        ("KM72jb", (32.041667, 34.75)),
        ("KM72JB", (32.041667, 34.75)),
    ]

    for sq, res in squares:
        loc = square_to_location(sq)
        # print(f'{sq}: {res}, calculated: {loc}')
        assert res == loc


def test_square_to_location_negative():
    squares = [
        ("KM32", "None"),
        (None, ""),
        ("KM32jn", (32.541667, 26.65000)),
        ("KM72kk", (32.416667, 34.73000)),
        ("JN45fo", (45.583333, 8.316000)),
        ("KO92so", (52.583333, 39.40000)),
        ("KM72jb", (32.041667, 34.65000)),
    ]

    for sq, res in squares:
        loc = square_to_location(sq)
        # print(f'{sq}: {res}, calculated: {loc}')
        assert res != loc
