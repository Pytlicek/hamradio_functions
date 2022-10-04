import pytest

from src.qth_locator import location_to_square


def test_location_to_square_positive():
    squares = [
        ("KM32jn", (32.541667, 26.75)),
        ("KM32jn", (32.570831, 26.750003)),
        ("KM72kk", (32.437487, 34.875015)),
        ("JN45fo", (45.603333, 8.456667)),
        ("KO92so", (52.601484, 39.565160)),
        ("KM72jb", (32.071209, 34.780089)),
        ("KM72jb", (32.07, 34.78)),
    ]
    for sq, loc in squares:
        qth = location_to_square(loc[0], loc[1])
        assert sq == qth

        if qth:
            assert len(qth) == 6


def test_location_to_square_assert():
    squares = [
        (None, (0, 0)),
        (None, (32, 26)),
    ]
    for sq, loc in squares:
        with pytest.raises(AssertionError) as excinfo:
            location_to_square(loc[0], loc[1])
            print("excinfo:", excinfo)
        assert excinfo.type == AssertionError


def test_location_to_square_negative():
    squares = [
        ("", (32.570831, 26.750003)),
        ("KM72kc", (32.437487, 34.875015)),
        ("JN45ff", (45.603333, 8.456667)),
        ("KO92cc", (52.601484, 39.565160)),
        ("KM72jj", (32.071209, 34.780089)),
    ]
    for sq, loc in squares:
        qth = location_to_square(loc[0], loc[1])
        assert sq != qth
