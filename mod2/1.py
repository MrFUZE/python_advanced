def get_summary_rss(file_path):
    with open(file_path) as f:
        lines = f.readlines()[1:]
        total_rss = sum(int(line.split()[5]) for line in lines)

    suffixes = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    i = 0
    while total_rss >= 1024 and i < len(suffixes) - 1:
        total_rss /= 1024
        i += 1

    return f"{total_rss:.2f} {suffixes[i]}"


if __name__ == '__main__':
    file_path = 'output_file.txt'
    summary_rss = get_summary_rss(file_path)
    print(f"Общее использование памяти RSS: {summary_rss}")
