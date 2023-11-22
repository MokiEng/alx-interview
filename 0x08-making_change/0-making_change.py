#!/usr/bin/python3
"""makeChange module."""


def makeChange(coins, total):
    """
    a method to return  fewest number of coins needed to meet total.
    """
    if total < 1:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
