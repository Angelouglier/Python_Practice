class Solution(object):
    def numJewelsInStones(self, J, S):
        count = 0
        for i in range(len(J)):
            count += S.count(J[i])
        return count
