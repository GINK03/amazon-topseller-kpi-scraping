import bottlenose
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import time
import os
import sys
import http.client
import urllib.request

CONF = dict( line.replace('\n', '').split(',') for line in open('credentials/keys') if line != '' )
print( CONF )
def error_handler(err):
  ex = err['exception']
  if isinstance(ex, HTTPError) and ex.code == 503:
    time.sleep(1) # 1秒待つ
    return True

if '--test' in sys.argv:
  # 本以外の角度では、asinコードとよばれるコードを持っていてそのコードでクエリを打って情報を取得する必要がある
  # asinは別途、取得するプログラムを書いたのでそちらを参照

  amazon = bottlenose.Amazon( CONF['ACCESS_KEY'], CONF['SECRET_ACCESS_KEY'], CONF['ASSOCIATE_TAG'], Region='JP', ErrorHandler=error_handler )

  # 商品情報のアトリビュート、属性情報、出版社、製造会社, title, auther, 大きさ、諸々
  # response = amazon.ItemLookup(ItemId="4774142298", ResponseGroup="ItemAttributes")
  # item_attr = BeautifulSoup(response,"lxml")
  # print(item_attr)

  # 類似商品の検索
  # top10の類似度の高い商品が帰ってくる
  # 類似度を算出するアルゴリズムは不明
  # response = amazon.ItemLookup(ItemId="4774142298", ResponseGroup="Similarities")
  # similarities = BeautifulSoup(response,"lxml")
  # for sim in similarities.findAll('title'):
  #  print(sim )

  # 特定のキーワードが所属しうる、カテゴリ名とブラウズノードIDを対応させて表示する
  ## ブラウズノードIDは商品のカテゴリみたいなもの
  response = amazon.ItemLookup(Keywords='任天堂', Operation='ItemSearch', ResponseGroup='BrowseNodes', SearchIndex='All')
  soup = BeautifulSoup(response, 'lxml')
  bnodeids = [ b.text for b in soup.findAll('browsenodeid') ]
  names = [ n.text for n in soup.findAll('name') ]
  pairs = dict(zip(names, bnodeids) )
  print(soup )
  print(pairs )
  # ブラウザノードIDの領域内でランキングを表示する
  response = amazon.ItemLookup(BrowseNodeId='503674', Operation='BrowseNodeLookup', ResponseGroup='TopSellers')
  soup = BeautifulSoup(response, 'lxml')
  print(soup)
  asins = [a.text for a in soup.findAll('asin') ]
  titles = [t.text for t in soup.findAll('title') ]
  pairs = dict(zip(asins, titles))
  print(pairs)

  """
  # レビューが書かれたurlを返却する.
  ## 商品レビューの内容はAPIが直接返してくれるわけでないので注意
  ## 商品情報のレビューのみを表示
  ## reviewでは、amp;optionがスマートフォンの読み込みを加速させる設定になっているので、これを無効にする必要がある
  response = amazon.ItemLookup(ItemId="482224816X", ResponseGroup="Reviews")
  reviews = BeautifulSoup(response,"lxml")
  for rev in reviews.findAll('iframeurl'):
    url = rev.text.replace('amp;', '')
    print( url )
    pages = urllib.request.urlopen(url).read().decode('utf8')
    # print( pages )
    soup = BeautifulSoup(pages, 'lxml')
    print( soup.text )
  """
