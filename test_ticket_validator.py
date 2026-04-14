import pytest
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

# Validate Ticket
def test_validation():
    assert validate_ticket("TK928450") == True

def test_too_long():
    assert validate_ticket("TK1234567") == False

def test_wrong_start():
    assert validate_ticket("QQ123456") == False


# calculate_total
def test_calculate_total():
    assert calculate_total([10, 20], 0.1)

def test_list_empty():
    with pytest.raises(ValueError):
        calculate_total ([], 0.1)

def test_not_list():
    with pytest.raises(TypeError):
        calculate_total("wrong", 0.1)