import subprocess

def process_count(username: str) -> int:
    ps_output = subprocess.check_output(['ps', '-u', username, '-o', 'user,command'])

    pids = subprocess.check_output(['pgrep', '-u', username]).decode().splitlines()

    return len(pids)


import subprocess

def total_memory_usage(root_pid: int) -> float:
    try:
        subprocess.check_call(['kill', '-0', str(root_pid)])
    except subprocess.CalledProcessError:
        raise ValueError('Process with pid {} does not exist'.format(root_pid))

    try:
        ps_output = subprocess.check_output(['ps', '--ppid', str(root_pid), '-o', 'rss'])
    except subprocess.CalledProcessError:
        return 0.0

    rss_list = ps_output.decode().split()[1:]
    rss_sum = sum(map(int, rss_list))

    meminfo_output = subprocess.check_output(['cat', '/proc/meminfo'])
    total_mem = int(meminfo_output.decode().split()[1]) * 1024.0

    return rss_sum / total_mem * 100.0
