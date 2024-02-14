#!/usr/bin/python3
"""
Primegame
"""


def is_prime(num):
    """
    Check if a number is prime
    """
    if num < 2:
        return False
        """
        Check divisibility from 2 to square root of num
        """
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    """
    Generate a list of prime numbers up to n
    """
    primes = []
    """
    Iterate from 1 to n (inclusive)
    """
    for i in range(1, n + 1):
        """
        Check if the number is prime and add it to the list if so
        """
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Determine the winner of the game
    """
    maria_wins = 0
    ben_wins = 0

    """
    Iterate through each round
    """
    for n in nums:
        """
        Get the list of prime numbers up to n
        """
        primes = get_primes(n)
        """
        If the number of primes is even, Ben wins
        """
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            """
            Otherwise, Maria wins
            """
            maria_wins += 1

    """
    Compare the number of wins for Maria and Ben
    """
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
