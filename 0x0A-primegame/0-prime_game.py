#!/usr/bin/python3
"""A Prime Game module."""


def isWinner(x, nums):
    """
    A function that returns name of the player
    that won the most rounds.
    """
    def is_prime(n):
        """To check prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """To get prime."""
        primes = []
        for i in range(1, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def game_winner(n):
        primes = get_primes(n)
        count = 0
        for p in primes:
            count += 1
            n -= p
        return "Maria" if count % 2 == 1 else "Ben"

    winners = [game_winner(n) for n in nums]

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
