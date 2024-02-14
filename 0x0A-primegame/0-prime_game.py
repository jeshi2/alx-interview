#!/usr/bin/python3
"""
Primegame number
"""


def isWinner(x_rounds, num_list):
    """
    Determines the winner of the Prime Game
    """
    """
    Check for invalid inputs
    """
    if not num_list or x_rounds < 1:
        return None

    """
    Find the maximum number in the list
    """
    max_num = max(num_list)

    """
    Initialize a list to mark prime numbers
    """
    primes = [True for _ in range(max(max_num + 1, 2))]

    """
    Use the Sieve of Eratosthenes algorithm to mark non-prime numbers
    """
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not primes[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            primes[j] = False

    """
    Set 0 and 1 as non-prime
    """
    primes[0] = primes[1] = False

    """
    Count the number of primes up to each index
    """
    prime_count = 0
    for i in range(len(primes)):
        if primes[i]:
            prime_count += 1
        primes[i] = prime_count

    """
    Determine the winner for each round
    """
    winner = ''
    player1_score = 0
    for n in num_list:
        player1_score += primes[n] % 2 == 1

    """
    Decide the overall winner based on scores
    """
    if player1_score * 2 == len(num_list):
        winner = None
    elif player1_score * 2 > len(num_list):
        winner = "Maria"
    else:
        winner = "Ben"

    return winner
