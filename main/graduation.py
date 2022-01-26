"""
Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal
Test cases:

for 5 days: 14/29

for 10 days: 372/773
"""


def calc_prob(n):

    if n == 0:
        #edge case handle
        return -1
    elif n < 4:
        # student cannot miss
        return f"{(2**n)/2}/{(2**n)}"

    res = [0 for i in range(n + 1)]
    present = list(res)
    res[4] = 1
    for i in range(5, n + 1):
        res[i] = (2 ** (i - 4)) + res[i - 4] + res[i - 3] + res[i - 2] + res[i - 1]
    for i in range(1, n + 1):
        present[i] = (2 ** i) - res[i]
    fail = present[n] - present[n - 1]
    return f"{fail}/{present[-1]}"

if __name__ == "__main__":
    print(calc_prob(5))
    print(calc_prob(10))