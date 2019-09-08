print(2**3)
print(2^3)

def raise_to_power(basu_number, power_number):
    result = 1
    for index in range(power_number):
        result = result * basu_number
    return result

print(raise_to_power(3,2))