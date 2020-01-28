class Solution:
    def intToRoman(self, num: int) -> str:
        kilo_map = {1: 'M', 2: 'MM', 3: 'MMM'}
        cent_map = {
            1: 'C', 2: 'CC', 3: 'CCC',
            4: 'CD', 5: 'D', 6: 'DC',
            7: 'DCC', 8: 'DCCC', 9: 'CM',
        }
        tens_map = {
            1: 'X', 2: 'XX', 3: 'XXX',
            4: 'XL', 5: 'L', 6: 'LX',
            7: 'LXX', 8: 'LXXX', 9: 'XC'
        }
        unit_map = {
            1: 'I', 2: 'II', 3: 'III',
            4: 'IV', 5: 'V', 6: 'VI',
            7: 'VII', 8: 'VIII', 9: 'IX'
        }

        ans = []

        kilo = num // 1000
        if kilo:
            ans.append(kilo_map[kilo])
        num -= kilo * 1000

        cent = num // 100
        if cent:
            ans.append(cent_map[cent])
        num -= cent * 100

        tens = num // 10
        if tens:
            ans.append(tens_map[tens])
        num -= tens * 10

        unit = num // 1
        if unit:
            ans.append(unit_map[unit])
        return ''.join(ans)


def test_solution():
    assert Solution().intToRoman(3) == 'III'
    assert Solution().intToRoman(4) == 'IV'
    assert Solution().intToRoman(9) == 'IX'
    assert Solution().intToRoman(58) == 'LVIII'
    assert Solution().intToRoman(1994) == 'MCMXCIV'
