class Solution(object):
    @staticmethod
    def half(x1, x2):
        return 1.0 * (x1 + x2) / 2

    @staticmethod
    def distance(x1, x2):
        import math
        return math.sqrt((x1[0]-x2[0]) * (x1[0]-x2[0]) + (x1[1]-x2[1]) * (x1[1]-x2[1]))

    @staticmethod
    def check_one(p1, p2, p3, p4):
        if Solution.half(p1[0], p2[0]) == Solution.half(p3[0], p4[0]) and Solution.half(p1[1], p2[1]) == Solution.half(p3[1], p4[1]):
            if Solution.distance(p1, p3) == Solution.distance(p1, p4) and Solution.distance(p1, p2) == Solution.distance(p3, p4):
                return 1
            return 0
        return 2

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if len(set((p1[0], p2[0], p3[0], p4[0]))) == 1: return False
        if len(set((p1[1], p2[1], p3[1], p4[1]))) == 1: return False

        res =  Solution.check_one(p1, p2, p3, p4)
        if res == 1: return True
        if res == 0: return False

        res =  Solution.check_one(p1, p3, p2, p4)
        if res == 1: return True
        if res == 0: return False

        res =  Solution.check_one(p1, p4, p3, p2)
        if res == 1: return True
        if res == 0: return False
        return False
