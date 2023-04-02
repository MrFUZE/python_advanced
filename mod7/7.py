import logging
import string


class PrintableASCIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return all(c in string.printable for c in record.msg)