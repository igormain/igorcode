def not_primes(a, b):
    list_numbers = []
    allowed_digits = "2357"
    
    for i in range(a, b):
        flag = True  
        for s in str(i):
            if s not in allowed_digits:
                flag = False  
                break  
        if flag and not is_prime(i):  
            list_numbers.append(i)
    return list_numbers


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(0.5)+1)):
        if n % i == 0:
            return False
    return True
    
