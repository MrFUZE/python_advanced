import sys

class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.stdout = stdout
        self.stderr = stderr
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

    def __enter__(self):
        if self.stdout:
            sys.stdout = self.stdout
        if self.stderr:
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_value, traceback):
        if self.stdout:
            sys.stdout = self.old_stdout
        if self.stderr:
            sys.stderr = self.old_stderr
        return False
