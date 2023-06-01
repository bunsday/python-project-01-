import string
import random

def scramble_email(email: str) -> str:
    head, tail = email.split('@')
    c1, c2, c3 = random.sample(string.ascii_lowercase + string.digits, 3)
    i = random.randint(1, max(1, len(head)-2))
    return  f'{c1}{head[:i]}{c2}{head[i:]}{c3}@{tail}'








