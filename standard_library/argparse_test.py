# ライブラリインポート
import argparse

# パーサ作成
parser = argparse.ArgumentParser(description='プログラム説明')


# 受け取る引数の追加
parser.add_argument('arg1', help='引数の説明')
parser.add_argument('arg2', help='引数の説明2')
parser.add_argument('--arg3') # オプション引数（指定しなくてもいい引数）を追加
parser.add_argument('-a', '--arg4') # よく使う引数なら省略形があると使うときに便利
parser.add_argument('--message', default='hello!') # デフォルト値
parser.add_argument('--number', type=int) # 型指定して変換（int）
parser.add_argument('--alpha', type=float, default=0.001) # 型指定して変換(float)
# リストで受け取る
tp = lambda x:list(map(int, x.split('.')))
parser.add_argument('--address', type=tp, help='IP address')
# フラグに使用(actionを指定)
parser.add_argument('--flag', action='store_true')
# 選択肢から選ばせる
parser.add_argument('--fruit', choices=['apple', 'grape', 'lemon'])
# 不定個数受け取る
parser.add_argument('--colors', nargs='*')
# オプション指定の必須引数
parser.add_argument('-requirement', required=True)


# 引数の解析
args = parser.parse_args()

print(f'arg1={args.arg1}')
print(f'arg2={args.arg2}')
print(f'arg3={args.arg3}')
print(f'arg4={args.arg4}')
print(f'message='+args.message)
print(f'number={args.number}')
print(f'alpha={args.alpha}')
print(f'address={args.address}')
print(f'is_flag={args.flag}')
print(f'fruit={args.fruit}')
print(f'colors={args.colors}')
print(f'requirement={args.requirement}')