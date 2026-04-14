
def validate_ticket(code):
    if not isinstance(code, str):
        raise TypeError
    if len(code) != 8:
        return False
    if not code.startswith("TK"):
        return False

def get_ticket_tier(code):
    if not validate_ticket(code):
        raise ValueError
    num = int(code[2])

    if num <= 3:
        return "General"
    elif num <=6:
        return "VIP"
    else:
        return "Platinum"

def calculate_total(prices, discount=0):
    if not isinstance(prices, list):
        raise TypeError
    if not prices:
        raise ValueError
    total = sum (prices)
    return round(total)