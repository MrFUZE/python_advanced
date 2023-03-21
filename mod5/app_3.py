class BlockErrors:
    def __init__(self, ignored_errors):
        self.ignored_errors = ignored_errors

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and exc_type not in self.ignored_errors:
            raise exc_val
        return True
