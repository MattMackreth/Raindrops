import pytest
from RaindropsMain import *
# Import necessary modules


# First test the 3 basic cases and the no factor case
def test_factor3():
    assert convert_number(6) == "Pling"


def test_factor5():
    assert convert_number(10) == "Plang"


def test_factor7():
    assert convert_number(14) == "Plong"


def test_no_factor():
    assert convert_number(2) == "2"



