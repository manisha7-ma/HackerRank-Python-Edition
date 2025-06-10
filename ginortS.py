input_str = input()
lowercase = [c for c in input_str if c.islower()]
uppercase = [c for c in input_str if c.isupper()]
digits    = [int(c) for c in input_str if c.isdigit()]

lowercase.sort()
uppercase.sort()
digits.sort()
n1=(i for i in digits if i%2!=0)
n2=(i for i in digits if i%2==0)
s=''.join(c for c in lowercase)
s2=''.join(c for c in uppercase)
s3=''.join(str(c) for c in n1)
s4=''.join(str(c) for c in n2)

print(s+s2+s3+s4)
