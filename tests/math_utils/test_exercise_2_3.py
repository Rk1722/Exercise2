from typing import Literal
import pytest
import os
import sys


def test_import_isprime():
    from math_utils.primes import isprime


@pytest.mark.parametrize("value, prime", [(1, False),
                                          (2, True),
                                          (3, True),
                                          (4, False),
                                          (47, True),
                                          (100, False)])
def test_isprime(value: Literal[1, 2, 3, 4, 47, 100], prime: bool):
    from math_utils.primes import isprime

    assert isprime(value) == prime, "Incorrect return value from isprime"

