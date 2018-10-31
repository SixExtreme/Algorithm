class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        tail, words = 'a', S.split()
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i, word in enumerate(words):
            if word[0].lower() in vowels:
                words[i] = word + 'ma'
            else:
                words[i] = word[1:] + word[0] + 'ma'
            tail, words[i] = tail + 'a', words[i] + tail

        return ' '.join(words)

if __name__ == '__main__':
    S = "I speak Goat Latin"
    print(Solution().toGoatLatin(S))