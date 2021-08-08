import re

text = "Email your feed back : book@subeen.com book@subeen aslo you can reffern anyone into thid mail info@service-shakil.com and you can use service.yes at khan dot com the bariar of khan at gmail dot com agamin email py.book@subeen.com"

#convert all kind of at into @
text = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+', '@', text, flags=re.I)

#convert all kind of dot into '.'
text = re.sub(r'\s+[\(\[]*\s*dot\s*[\)\]]*\s+', '.', text, flags=re.I)

#Regular expression for finding email address
result = re.findall(r'([.\w]+@\w+\-*\w+[.]\w+)', text)

print(result)
