import re

text = "abc@gmail.com xyz@yahoo.com"

emails = re.findall(r'\S+@\S+', text)

for email in emails:
    print(email)