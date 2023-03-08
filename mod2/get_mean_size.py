import sys

def get_mean_size():
    lines = sys.stdin.readlines()[1:]
    total_size = 0
    num_files = 0
    for line in lines:
        tokens = line.split()
        if len(tokens) > 4:
            try:
                size = int(tokens[4])
                total_size += size
                num_files += 1
            except ValueError:
                pass
    if num_files > 0:
        mean_size = total_size / num_files
        print(mean_size)

if __name__ == '__main__':
    get_mean_size()
