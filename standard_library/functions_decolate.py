from functools import lru_cache
from contextlib import contextmanager
import os

# lru_cache ：関数の結果をキャッシュし、同じ引数で呼び出された場合に計算を省略できる（爆速になる）

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(100))

# contextmanager：ジェネレータ関数からコンテキストマネージャーを簡単に作成できる
@contextmanager
def tempdir():
    print("一時ディレクトリを作成")
    try:
        yield "temp_dir_path"
    finally:
        print("一時ディレクトリを削除")
        
with tempdir() as temp_path:
    print(f"一時ディレクトリ {temp_path} で作業中")
    
@contextmanager
def change_directory(new_dir):
    current_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(current_dir)

# 使用例
with change_directory('/tmp'):
    print("Current directory:", os.getcwd())