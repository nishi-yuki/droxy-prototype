#! /usr/bin/env python3
# vim :setfiletype python3

''' Droxy Prototype

Proxy設定をssidごとに行うツールdroxyのプロトタイプ版です。プロトタイプ版なので
日本語が多いです。コメントもゆるふわです。ゆるしてね。
'''

import argparse
import sys
DROXY_CMD_NAME = 'droxy'


def main():
    name_called = sys.argv[0]

    if name_called == DROXY_CMD_NAME:
        # コマンドのラッパーとしてではなくdroxy自体を呼び出された。
        droxy_cmd_handler()
    else:
        # 他のシェルコマンドのラッパーとしてソフトリンク経由で呼び出された。
        call_cmd(name_called)


def droxy_cmd_handler():
    """　"$ droxy" で呼び出された関数の中身

    droxy_cmd_handlerはdroxyコマンドを呼び出されたときに実行される関数です。\
    droxyコマンドはdroxy自体の操作を行います。
    """
    pass


def call_cmd(cmd_name: str):
    """ シェルコマンドの呼び出し
    
    call_cmd は cmd_name で指定されたシェルコマンドにプロクシ設定を施した上で\
    実行する関数です。

    Args:
        cmd_name (str): 呼び出すシェルコマンド
    
    Returns:
        int: ステータスコード
    """
    pass


def command(name: str):
    """ シェルコマンドラッパー関数を登録するデコレータ

    Args:
        name (str): コマンド名
        pythonの関数名で使用可能な文字集合とコマンド名として\
        使用可能な文字集合は異なるため、このような引数を必要とします。
    """