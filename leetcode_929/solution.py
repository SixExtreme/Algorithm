class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        counter = set()
        for email in emails:
            name, domain, *_ = email.split('@')
            name, *_ = name.split('+')
            name = name.replace('.', '')
            email = "{}@{}".format(name, domain)
            counter.add(email)
        return len(counter)

