#!/usr/bin/python3
"""
Primegame
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]

    def optimal_strategy(primes):
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = []
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        winner = optimal_strategy(primes)
        winners.append(winner)

    ben_wins = winners.count("Ben")
    maria_wins = winners.count("Maria")

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None