import re

with open('file.html','r') as f:
    text = f.read()

pattern = re.compile(r'<li>\s+(.*?)\s+<ol>\s+<li>(.*?)</li>\s+<li>(.*?)</li>')
information = pattern.findall(text, re.M)


for info in information:
    print(info[0] + " - " + info[1] + " , " + info[2])