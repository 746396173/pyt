import re

pattern = r"[\w]{4,20}@163\.com$"#字符串结尾必须与$前一致
s = "1566544@163.com45456"
result = re.match(pattern,s)
print(result)
pattern = r"[\w]{4,20}@163\.com"#字符串结尾必须与$前一致
result =re.match(pattern,s)
print(result)


pattern = r"\\n"#第一个\用于转义正则表达式的\n
s = r"\n"
result = re.match(pattern,s)
print(result)
