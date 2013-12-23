# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='簡単な例です') # parserを作る
parser.add_argument('bar')         # 引数を追加します
parser.add_argument('-f', '--foo') # オプションを追加します
parser.add_argument('-r', required=True) # このオプションは必須です
parser.add_argument('--version', action='version', version='%(prog)s 2.0') # version
args = parser.parse_args() # コマンドラインの引数を解釈します

print(args)
