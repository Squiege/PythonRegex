# Task 1
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

def find_by_domain():
    exclude = re.findall(r"\b[A-Za-z0-9._%+-]+@[domain]+[A-Z|a-z]{2,}\b", text)
    print(exclude)

find_by_domain()
print(emails)