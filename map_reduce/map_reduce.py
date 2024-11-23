from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

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

# 実行例
if __name__ == "__main__":
    input_data = ["Hello world"
                  ,"Hello Python"
                  ,"MapReduce is powerful"
                  ,"Python is awesome"
                  ,"Big data processing with MapReduce"
                  ,"Districted computing and parallel processing"
                  ,"Data analysis using MapReduce paradigm"
                  ,"Efficient data processing with Python"
                  ]
    result = map_reduce(input_data)
    for word, count in sorted(result, key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")