# Amazon TopSeller KPI Scraping

## Amazom APIとは
Amazon JPが提供するAmazon APIについて記述します。  
Amazon APIは、商品の情報を取得することができるAPIで取得する代表的な情報の角度は以下の通りです
```console
1. 特定の単語がどの商品カテゴリ(ブラウズIDなどと呼ばれる)に属するか
2. 商品カテゴリごとのランキング情報Top10
3. 商品のIDごとのアトリビュート（値段や製造メーカや様々な情報）
4. 商品のIDごとのレビュー情報
```
機械学習を用いたマーケティングとして有益な情報の角度としては、ランキング情報が間接的に世の中の市況を表現すると考えれられるので、何かしら使えるという印象があります  

また、商品の口コミ情報も何か使えると思います   

## Amazon APIの制限
使用頻度を見ている限り、１分間に一回以上実行すると、503エラー（頻度が多すぎるエラー）が出るというものなので、制約は結構厳しいです  

## 実際のランキング情報取得フロー
- 1. 欲しいキーワードの一覧を得る
- 2. キーワード一覧から、それが所属する商品カテゴリを検索する
- 3. 商品カテゴリからランキングを取得する
- 4.　必要に応じて、商品の口コミ情報を取得する

## プログラムの実行例
あらかじめ、keysというファイルをcredentials　のディレクトリに入れておく必要があります　　　
keysには、AWSのアクセスキーと、シークレットキーと、ユーザ名を記す必要があります  

商品のアトリビュートを表示
```console
$ python3 examples.py '--attribute'
```
サンプル出力結果
```console
<idtype>ASIN</idtype><itemid>4774142298</itemid>
<responsegroup>ItemAttributes</responsegroup>
<asin>4774142298</asin>
<url>https://www.amazon.co.jp/gp/pdp/taf/4774142298</url>
<itemattributes>
  <author>辻 真吾</author>
  <binding>大型本</binding>
  <ean>9784774142296</ean>
  <isbn>4774142298</isbn>
  <label>技術評論社</label>
  <language><name>日本語</name><type>Published</type></language>
  <manufacturer>技術評論社</manufacturer>
  <numberofpages>320</numberofpages>
  <height units="100分の1インチ">87</height>
  <length units="100分の1インチ">898</length>
  <weight units="100分の1ポンド">123</weight>
  <width units="100分の1インチ">724</width>
  <publisher>技術評論社</publisher>
  <studio>技術評論社</studio>
  <title>Pythonスタートブック</title>
</itemattributes>
```

類似商品トップ１０を表示
```console
$ python3 examples.py '--similarities'
```
キーワードが所属しやすいカテゴリ一覧を検索
```console
$ python3 examples.py '--categories'
```
カテゴリごとの売り上げランキングを表示
```console
$ python3 examples.py '--topseller'
```
レビュー情報の取得
```console
$ python3 examples.py '--reviews'
```
