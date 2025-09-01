import re

text = "Email: test@example.com, backup: admin@example.org"
match = re.findall(r'\S+@\S+', text)

if match:
    print("Found:", match)
