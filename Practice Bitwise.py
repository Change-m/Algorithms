# Find the reverse bits
class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        out = 0
        for _ in range (31):
            bit = n & 1
            out |= bit
            out <<= 1
            n >>= 1
        out |= n
        return out
