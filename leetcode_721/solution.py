from typing import List, Dict, Set, Deque
from collections import deque


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_map: Dict[str, List[int]] = dict()
        for i, account in enumerate(accounts):
            _, *email_set = account
            for email in email_set:
                if email not in email_map:
                    email_map[email] = []
                email_map[email].append(i)
        print(email_map)

        node_map: Dict[int, Set[int]] = dict()
        for i, account in enumerate(accounts):
            if i not in node_map:
                node_map[i] = set()
            _, *email_set = account
            for email in email_set:
                for j in email_map[email]:
                    if j != i:
                        node_map[i].add(j)
        print(node_map)

        for key in list(node_map.keys()):
            if key not in node_map:
                continue
            queue: Deque[int] = deque(node_map[key])
            while queue:
                node: int = queue.popleft()
                if node == key:
                    continue
                node_map[key].add(node)
                if node in node_map:
                    queue.extend(node_map[node])
                    del node_map[node]
        print(node_map)

        ans: List[List[str]] = []
        for key in node_map:
            account = accounts[key][0]
            email_set = set(accounts[key][1:])
            for node in node_map[key]:
                email_set |= set(accounts[node][1:])
            emails = list(email_set)
            emails.sort()
            ans.append([account, *emails])
        return ans


def test_solution():
    # accounts = [
    #     ["John", "johnsmith@mail.com", "john00@mail.com"],
    #     ["John", "johnnybravo@mail.com"],
    #     ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    #     ["Mary", "mary@mail.com"]
    # ]
    # print(Solution().accountsMerge(accounts))

    accounts = [
        ["David", "David0@m.co", "David1@m.co"],
        ["David", "David3@m.co", "David4@m.co"],
        ["David", "David4@m.co", "David5@m.co"],
        ["David", "David2@m.co", "David3@m.co"],
        ["David", "David1@m.co", "David2@m.co"]
    ]
    print(Solution().accountsMerge(accounts))
