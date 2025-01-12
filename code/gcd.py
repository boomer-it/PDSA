from factors import factors
from check_prime import check_prime

# If one number has a certain set of factors
# and second number has a certain set of factors
# then you just have to get the highest common number from the two sets.
num1 = 12
num2 = 8
factors_1 = factors(num1)
factors_2 = factors(num2)
common_factors = []
for i in factors_1:
    if i in factors_2:
        common_factors.append(i)
gcd = max(common_factors)
print(gcd)


