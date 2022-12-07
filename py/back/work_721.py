from pprint import pprint
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        val = sorted(accounts, key=lambda x: x[0])
        output = [val[0]]
        for x in val[1:]:
            flag_match = False
            for y in output:
                if x[0] == y[0]:
                    if any(tmp in y[1:] for tmp in x[1:]):
                        y.extend(x[1:])
                        flag_match = True
                        break
            if not flag_match:
                output.append(x)
        for x in output:
            x[1:] = sorted(list(set(x[1:])))
        print 'myoutput is:'
        pprint(output)
        return output





