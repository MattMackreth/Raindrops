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


# Tests to ensure factors themselves work
def test_self3():
    assert convert_number(3) == "Pling"


def test_self5():
    assert convert_number(5) == "Plang"


def test_self7():
    assert convert_number(7) == "Plong"


# Then tests for combinations of factors
def test_factor3_5():
    assert convert_number(15) == "PlingPlang"


def test_factor3_7():
    assert convert_number(21) == "PlingPlong"


def test_factor5_7():
    assert convert_number(35) == "PlangPlong"


def test_factor3_5_7():
    assert convert_number(105) == "PlingPlangPlong"


# Testing for borderline cases of negatives, 1 and 0
def test_negative_case():
    assert convert_number(-6) == "Pling"


def test_one_case():
    assert convert_number(1) == "1"


# Mathematically 0 has infinite factors so all strings should be returned
def test_zero_case():
    assert convert_number(0) == "PlingPlangPlong"


# Datatype testing:
# Tests for borderline datatypes of decimal and integer as string
def test_decimal():
    assert convert_number(12.1234) == "12.1234"


def test_num_as_string():
    assert convert_number("2") == "2"


# Tests to ensure function does not take non-number inputs
def test_string():
    with pytest.raises(TypeError):
        convert_number("Hello World")
