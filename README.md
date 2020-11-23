# Yahoo!形態素解析APIを使用するためのサンプル

# 使い方

1. `pip install -r requirements.txt` で必要なパッケージをインストールする
2. ファイル `.env.example` をコピーして、ファイル `.env` を作成する
3. `CLIENT_ID=` に自分のYahoo!アプリケーションのクライアントIDを記入する
4. `python main.py` で実行する

# デバッグモード

デバッグモード（実際にAPIを使用せずに、サンプルのXMLを使用する）場合は、
`.env` の `DEBUG=` を `True` にする。
※ `DEBUG=` に何かしらの文字列が入っている場合に、
デバッグモードになるので、APIを使用したい場合は `DEBUG=` は何も指定しない。
