import logging
import getpass
import hashlib


def input_and_check_password():
    password: str = getpass.getpass()
    if not password:
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode("latin-1"))
        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError:
        pass
    return False


if __name__ == "__main__":
    logging.basicConfig(
    filename='stderr.txt',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%H:%M:%S'
    )
    count_number: int = 3
    while count_number > 0:
        if input_and_check_password():
            logging.info('Password is correct')
            exit(0)
        count_number -= 1
    logging.info('Password is incorrect')
    exit(1)
