import requests
from bs4 import BeautifulSoup
import time
import os
from selenium import webdriver

print("クローリング開始")

# ファイル保存用ディレクトリの作成
dir_name = "./filmarks_files"
os.mkdir(dir_name)

# htmlファイル保存用ディレクトリの作成
dir_name = "./filmarks_files/html_files"
os.mkdir(dir_name)

# javascriptで動かした後のhtmlを取るためPhantomJSを使用
driver = webdriver.PhantomJS()
# 1ページ目をhtml化
first_url = "https://filmarks.com/list/country/5"
driver.get(first_url)
time.sleep(1)
first_html = driver.page_source

# ファイルに保存
page_count = 1    # ページ数カウント
with open('./filmarks_files/html_files/page{}.html'.format(page_count), 'w', encoding='utf-8') as f:
    f.write(first_html)

# 検収条件のための総映画本数を取得
soup = BeautifulSoup(first_html, "lxml")
total_num = soup.find("h1", class_="c-heading-1").text
print(total_num)
# 総映画本数をテキストファイル1行目に保存
path_to_txt = './filmarks_files/data.txt'
with open(path_to_txt,'w') as f:
    f.write("{}\n".format(total_num))

# 2ページ目以降のクローリング,次ページがなくなるまで続ける
while True:
    page_count += 1

    # 次ページに進むurlを探す
    next_url = soup.find("a", class_="c-pagination__next")

    # 次ページがなければ終了
    if next_url == None:
        print("総ページ数:", page_count-1)
        with open(path_to_txt,'a') as f:
            f.write("総ページ数:{}\n".format(page_count-1)) #テキストファイル2行目に総ページ数保存
        print("{}ページ完了".format(page_count-1))
        print("クローリング終了")
        break

    # 次ページurlを取得しhtmlファイルとして保存
    url = next_url.get("href")
    url = "https://filmarks.com"+url  # urlの先頭が抜けているので補う
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    with open("./filmarks_files/html_files/page{}.html".format(page_count), "w", encoding='utf-8') as f:
        f.write(html)

    # 次ページのurlを取得するために解析準備
    soup = BeautifulSoup(html, "lxml")

    # クローリング進捗の出力
    if page_count % 10 == 0:
        print(page_count, "ページ完了")
