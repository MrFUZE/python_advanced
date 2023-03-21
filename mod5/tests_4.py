import io
import sys

def test_redirect_stdout():
    stdout_file = io.StringIO()
    with Redirect(stdout=stdout_file):
        print('Hello, stdout!')
    assert stdout_file.getvalue() == 'Hello, stdout!\n'

def test_redirect_stderr():
    stderr_file = io.StringIO()
    with Redirect(stderr=stderr_file):
        raise ValueError('Hello, stderr!')
    assert 'Hello, stderr!' in stderr_file.getvalue()

def test_redirect_stdout_and_stderr():
    stdout_file = io.StringIO()
    stderr_file = io.StringIO()
    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello, stdout!')
        raise ValueError('Hello, stderr!')
    assert stdout_file.getvalue() == 'Hello, stdout!\n'
    assert 'Hello, stderr!' in stderr_file.getvalue()

def test_no_redirect():
    stdout_file = io.StringIO()
    stderr_file = io.StringIO()
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    with Redirect():
        pass
    assert sys.stdout == old_stdout
    assert sys.stderr == old_stderr

def test_redirect_stdout_only():
    stdout_file = io.StringIO()
    old_stdout = sys.stdout
    with Redirect(stdout=stdout_file):
        pass
    assert sys.stdout == old_stdout

def test_redirect_stderr_only():
    stderr_file = io.StringIO()
    old_stderr = sys.stderr
    with Redirect(stderr=stderr_file):
        pass
    assert sys.stderr == old_stderr
