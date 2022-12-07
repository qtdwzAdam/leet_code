


class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """

        len_cnt = len(customers)
        close_time = 0
        close_cost = customers.count('Y')
        last = close_cost
        for idx in range(1, len_cnt+1):
            val = customers[idx-1]
            if val == 'N':
                now = last + 1
            else:
                now = last - 1
            last = now
            if now < close_cost:
                close_cost = now
                close_time = idx
            # print(idx, now, close_time, close_cost)
        return close_time

def main():
    print('start')
    x = Solution().bestClosingTime('YYNY')
    print(x, x==2)
    x = Solution().bestClosingTime('NNNNN')
    print(x, x==0)
    x = Solution().bestClosingTime('YYYY')
    print(x, x==4)
    x = Solution().bestClosingTime('YYYYNNNNYYYNYNYNYNYYYNYNYNYYYYNYNYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
    print(x, x==72)



if __name__ == '__main__':
    main()
    print('end')