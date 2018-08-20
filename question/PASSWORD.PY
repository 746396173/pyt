'''斯蒂芬和索菲亚忘记了安全性，并使用简单的密码。
帮助Nikola开发密码安全检查模块。
如果密码的长度大于或等于10个符号，密码将被认为足够强，它至少有一个数字，
并且其中包含一个大写字母和一个小写字母。
密码仅包含ASCII拉丁字母或数字。
Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
'''
import string

upper = set(string.ascii_uppercase)
lower = set(string.ascii_lowercase)
digits = set(string.digits)


def checkio(data):
    'Return True if password strong and False if not'
    letters = set(data)
    return bool(
        len(data) >= 10 and upper & letters and lower & letters
        and digits & letters)


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, 'First'
    assert checkio('bAse730onE4') == True, 'Second'
    out =  checkio(input("0000"))
    print(out)
    print('All ok')