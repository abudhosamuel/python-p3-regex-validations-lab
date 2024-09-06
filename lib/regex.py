import re

# Regular expression for name, accounting for names with hyphens and apostrophes
name = r"^[A-Z][a-z]+(?:'[A-Z][a-z]+)?(?: [A-Z][a-z]+)*(?:-[A-Z][a-z]+)*$"
name_regex = re.compile(name)

# Regular expression for phone number, accounting for numbers with or without delimiters
phone_number = r"^(\(\d{3}\) |\d{3}-|\d{10})\d{3}-?\d{4}$"
phone_regex = re.compile(phone_number)

# Regular expression for email address, allowing numbers at the start
email_address = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)
