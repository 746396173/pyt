'''You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105

您将获得一个文本，其中包含不同的英文字母和标点符号。
你应该在文中找到最常见的字母。
返回的信件必须是小写的。
在检查最想要的字母时，外壳无关紧要，因此为了您的搜索，“A”==“a”。
确保不计算标点符号，数字和空格，仅计算字母。
如果您有两个或多个频率相同的字母，请返回拉丁字母中首先出现的字母。
例如 - “one”每个只包含“o”，“n”，“e”一次，因此我们选择“e”。
'''
import string


def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

    