import re
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

def parse_log_line(line):
    pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(.+)\] "(\w+) (.+) HTTP/.*" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        ip, timestamp, method, path, status, size = match.groups()
        return ip, {
            'timestamp': timestamp,
            'method': method,
            'path': path,
            'status': int(status),
            'size': int(size)
        }
    return None, None

def map_function(item):
    # ここでマッピング処理を行う
    words = item.split()
    return [(word.lower(), 1) for word in words]

def reduce_function(item):
    # ここで集計処理を行う
    key, values = item
    return (key, sum(values))

def map_reduce(data, map_func=map_function, reduce_func=reduce_function, num_workers=None):
    if num_workers is None:
        num_workers = multiprocessing.cpu_count()

    # Map段階
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        mapped_data = list(executor.map(map_func, data))
    
    # データをグループ化
    grouped_data = defaultdict(list)
    for key, value in [item for sublist in mapped_data for item in sublist]:
        grouped_data[key].append(value)
        
    # Reduce段階
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        reduced_data = list(executor.map(reduce_func, grouped_data.items()))
        
    return reduced_data

# 使用例
if __name__ == '__main__':
    log_lines = [
        '192.168.0.1 [2023-05-01 12:00:00] "GET /index.html HTTP/1.1" 200 1024',
        '10.0.0.1 [2023-05-01 12:00:01] "POST /submit HTTP/1.1" 404 512',
        '192.168.0.1 [2023-05-01 12:00:02] "GET /about HTTP/1.1" 200 2048',
        '172.16.0.1 [2023-05-01 12:00:03] "GET /contact HTTP/1.1" 200 4096'
    ]

    parsed_data = [parse_log_line(line) for line in log_lines if parse_log_line(line)[0] is not None]
    result= map_reduce(parsed_data, map_func=map_function, reduce_func=reduce_function)
    for ip, count in result:
        print(f"IP: {ip}, Count: {count}")