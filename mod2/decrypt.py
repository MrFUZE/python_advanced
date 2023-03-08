import sys


def decrypt(cipher: str):
    result = []

    for i in cipher:
        result.append(i)
        if len(result) > 2 and (result[-1], result[-2]) == (".", "."):
            result.pop()
            result.pop()
            if result:
                result.pop()
    return "".join(i for i in result if i != ".")

if __name__ == '__main__':
    cipher = sys.stdin.read().strip()
    message = decrypt(cipher)
    print(message)
