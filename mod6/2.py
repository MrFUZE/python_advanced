import re


with open('/usr/share/dict/words', 'r') as f:
    words = [word.strip().lower() for word in f if len(word.strip()) > 4]


def is_strong_password(password: str) -> bool:
    password = password.lower()

    words = re.findall(r'\b\w+\b', password)

    for word in words:
        if len(word) > 4 and word in words:
            return False


    return True


# password = 'MyP@ssword123'
# if is_strong_password(password):
#     print('Password is strong')
# else:
#     print('Password is weak')
