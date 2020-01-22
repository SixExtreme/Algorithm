class Solution:
    def defangIPaddr(self, address: str) -> str:
        # return address.replace('.', '[.]')
        return '[.]'.join(address.split('.'))


def test_solution():
    assert Solution().defangIPaddr('1.1.1.1') == '1[.]1[.]1[.]1'
    assert Solution().defangIPaddr('255.100.50.0') == '255[.]100[.]50[.]0'
