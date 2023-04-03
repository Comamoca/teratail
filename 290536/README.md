# python　スクレイピング　エラー

[URL](https://teratail.com/questions/290536)

## 質問

- Pythonで`KeyError`

```
df_notnull['Title'].str.contains('Python超入門コース')
↓
KeyError: 'Title'
```

### 問題の詳細

詳しい詳細は無し

## 考えられる原因

- keyが間違ってるのでは
- 取得データにミス?
- 前の処理でデータを消してしまっているのでは(やりがち)

## 対応

- 前後の処理の確認
- 考えられる原因を潰す

## サンプルプログラムの実行方法

おまけ。[このサイト](https://blog.ablaze.one)のトップ記事のタイトルを取得する。

lxmlとBS4、Requestsで書いた。

### 実行方法

```
poetry install
poetry run python main.py
```

- requests
- bs4
- lxml

の3つがインストールされてれば実行できるはず。
