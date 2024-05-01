# Alternating Binary String

You are given a binary string S of length N.
You can perform the following operation on it:

- Choose an index i (1≤i≤N), and flip every character of S from index i to N.
- Flipping a character means turning it from 0 to 1 and vice versa.

For example, if S=1001101 and you choose i=4, the resulting string will be S=1000010.

Find the minimum number of operations required to turn S into an alternating string.
S is said to be an alternating string if Si≠Si−1​ for every i from 2 to N.
It can be proved that it's always possible to turn S into an alternating string.
