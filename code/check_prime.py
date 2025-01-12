from factors import factors
def check_prime(n):
    factor_list = factors(n)
    if len(factor_list) == 2:
        return True
    else:
        return False
print(check_prime(23))

