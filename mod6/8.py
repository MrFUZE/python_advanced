import re


def my_t9(digits):
    digit_map = {
        '2': '[abc]',
        '3': '[def]',
        '4': '[ghi]',
        '5': '[jkl]',
        '6': '[mno]',
        '7': '[pqrs]',
        '8': '[tuv]',
        '9': '[wxyz]'
    }

    pattern = ''.join(digit_map[d] for d in str(digits))
    regex = re.compile('^' + pattern + '$')

    with open('/usr/share/dict/words', 'r') as f:
        words = [line.strip() for line in f]

    return [word for word in words if regex.match(word)]


if __name__ == '__main__':
    print(my_t9(22736368))