import re
pattern=r"\b([a-z]+[A-Za-z0-9_.-]+@[a-zA-z0-9])" #(hcl)
pattern1=r"[7-9][0-9]{9}"
str1="hello from hcl hcl banglorehcl liki@gmail.com liki123@gmail 56556 38989"
m1=re.findall(pattern,str1)
m2=re.findall(pattern1,str1)
print((m1))
print(len(m2))
