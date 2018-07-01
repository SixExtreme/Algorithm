class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # counter = dict()
        # cpdomains = set(cpdomains)
        # for cpdomain in cpdomains:
        #     count, domain = cpdomain.split()
        #     count = int(count)
        #     if domain not in counter:
        #         counter[domain] = count
        #     else:
        #         counter[domain] += count

        #     *sub, first = domain.split('.')
        #     if first not in counter:
        #         counter[first] = count
        #     else:
        #         counter[first] += count

        #     if len(sub) > 1:
        #         _, second = sub
        #         subdomain = '{}.{}'.format(second, first)
        #         if subdomain not in counter:
        #             counter[subdomain] = count
        #         else:
        #             counter[subdomain] += count
        
        from collections import Counter
        counter = Counter()

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            counter[domain] += count
            for i, c in enumerate(domain):
                if c is '.':
                    counter[domain[i+1:]] += count

        return ['{} {}'.format(count, domain) for domain, count in counter.items()]

if __name__ == '__main__':
    cpdomains = ["9001 discuss.leetcode.com"]
    ret = Solution().subdomainVisits(cpdomains)
    print(ret)