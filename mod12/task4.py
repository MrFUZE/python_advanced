import datetime
import requests
import time

URL = "http://127.0.0.1:8080/timestamp/"
LOG_FILE = "log.log"


def write_log(timestamp):
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp}\n")


def get_timestamp():
    response = requests.get(URL)
    timestamp = response.text
    timestamp_datetime = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    return datetime.datetime.isoformat(timestamp_datetime)


def main():
    while True:
        try:
            timestamp = get_timestamp()
            write_log(timestamp)
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"error: {e}")


if __name__ == "__main__":
    main()
