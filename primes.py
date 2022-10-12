"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):

    if number_of_primes > 0:
        list = []
        numerator = 1
        while len(list) < number_of_primes:
            numerator = numerator+1
            for denominator in range (2,numerator):
                if (numerator%denominator == 0):
                    break
            else:
                list.append(numerator)
                print(numerator)
        return list

    if number_of_primes <= 0:
        raise ValueError ("Parameter must be greater than 0")



    #print(list)

#primes(-1)


    #except ValueError:
        #raise ValueError("Make sure you dont enter 0 or a negative number")
