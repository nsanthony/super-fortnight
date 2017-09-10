#! /home/nsanthony/anaconda3/bin/python


num_of_primes = 10000
prime_num_count = 0
primes = [0]*num_of_primes
i = 1 #starting prime


while prime_num_count < num_of_primes:
    i += 1
    divisible = 1
    k = 0
    while k < prime_num_count:
        if(i % primes[k] == 0): #modulus 
            divisible = 0
            break
        else:
            k += 1
    if divisible != 0:
        primes[prime_num_count] = i
        prime_num_count += 1
        print(i)
#print(primes[prime_num_count-1])