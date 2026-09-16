text_with_email_addresses = "Contact us at fake@email.d f@vdberg.us support@example.com or sales@example.com for more information."
text_with_urls = "Visit our website at https://example.com or follow us at http://twitter.com/example for updates."
text_with_ip_addresses = "The server IP addresses are 192.168.1.1, 10.0.0.1, and 172.16.0.1."
text_with_phone_numbers = "You can reach us at +1-800-555-1234 or +44 20 7946 0958."

import re

# general rules:
# .        Matches any single character
# \        Escapes one of the meta characters to treat it as a regular character
# \d       Matches any digit (equivalent to [0-9])
# \w       Matches any alphanumeric character (equivalent to [a-zA-Z0-9_])
# [...]    Matches a single character or a range that is contained within brackets. Order does not matter but without brackets order does matter
# +        Matches the preeceding element one or more times
# ?        Matches the preeceding element zero or one time
# *        Matches the preeceding element zero or more times
# {m,n}    Matches the preeceding element at least m and not more than n times
# ^        Matches the beginning of a line or string
# $        Matches the end of a line or string
# [^...]   Matches a single character or a range that is not contained within the brackets
# ?:...|..."Or" operator
# ()       Matches an optional expression


# extract all email addresses from the text
email_pattern = (r"[a-zA-Z0-9._%+-]+" # matches the local part of the email address
                 r"@" # matches the "@" symbol
                 r"[a-zA-Z0-9.-]+" # matches the domain name
                 r"\." # matches the dot before the domain suffix
                 r"[a-zA-Z]{2,}") # matches the domain suffix (2 or more characters)
email_addresses = re.findall(email_pattern, text_with_email_addresses)
print(email_addresses)


# extract all URLs from the text
url_pattern = (
    r"https?://" # matches "http://" or "https://"
    r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}" # matches the domain name and domain suffix
    r"(?::\d{1,5})?" # matches an optional port number
    r"(?:/[^\s?#]*)?" # matches an optional path
    r"(?:\?[^\s#]*)?" # matches an optional query string
    r"(?:#[^\s]*)?" # matches an optional fragment identifier
)
urls = re.findall(url_pattern, text_with_urls)
print(urls)


# extract all IP addresses from the text
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
ip_addresses = re.findall(ip_pattern, text_with_ip_addresses)
print(ip_addresses)


# extract all phone numbers from the text
phone_pattern = r"\+?\d[\d\s-]{7,}\d"
phone_numbers = re.findall(phone_pattern, text_with_phone_numbers)
print(phone_numbers)