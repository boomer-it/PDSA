from factors import factors
from check_prime import check_prime

prime_list = []
for i in range(1,101):
    if check_prime(i):
        prime_list.append(i)
print(prime_list)
