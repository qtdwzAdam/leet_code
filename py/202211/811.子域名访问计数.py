# coding=utf-8
#
# @lc app=leetcode.cn id=811 lang=python
#
# [811] 子域名访问计数
#

# @lc code=start
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        res = defaultdict(int)
        for x in cpdomains:
            x_cnt, x_domain = x.split(" ")
            x_cnt = int(x_cnt)
            x_domain_list = x_domain.split('.')[::-1]
            obj_domain = x_domain_list[0]
            for _x in x_domain_list[1:]:
                res[obj_domain] += x_cnt
                obj_domain = '%s.%s' % (_x, obj_domain)
            res[obj_domain] += x_cnt
        return ["%s %s" % (v, k) for k, v in res.items()]

if __name__ == "__main__":
    so = Solution()
    print so.subdomainVisits(["9001 discuss.leetcode.com"])
    print so.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])



        
# @lc code=end

