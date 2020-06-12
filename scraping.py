from bs4 import BeautifulSoup
import csv
import datetime
import re


print("スクレイピング開始")

# csvファイルにヘッダー付ける
with open("./filmarks_files/film_data.csv", "w", newline="", encoding='CP932') as f:
    header = ["No.", "name", "release_date", "screening_time", "rate", "view", "clip", "total",
    "anime", "drama", "romance", "horror", "art", "war", "music", "musical", "sports", "SF", "youth", "comedy", "action", "adventure", "crime", "documentary", "suspence", "shortfilm",
    "family", "thriller", "zidai_geki", "fantasy", "yakuza", "mystery","biography", "western", "panic", "omnibus", "violence", "history", "gang",
    "vod", "director", "screenwriter", "starring"]
    writer = csv.DictWriter(f, header)
    writer.writeheader()

#総ページ数を取る
with open("./filmarks_files/data.txt") as f:
    data = f.readlines()
    total_num = int(re.sub("\\D", "", data[0]))
    total_page = int(re.sub("\\D", "", data[1]))

# 作品数カウンタの初期化
film_count = 0
# 1ページに20作品掲載されているページ数を数えるカウンタの初期化(検収条件で使用)
kenshu_count = 0

for page_num in range(total_page):
    # スクレイピングの進捗出力
    if page_num % 10 == 0:
        print(page_num, '/', total_page)

    # スクレイピングするhtmlファイルをで開く
    with open("./filmarks_files/html_files/page{}.html".format(page_num + 1), "r", encoding="utf-8") as f:
        page = f.read()
    soup = BeautifulSoup(page, "lxml")

    # 作品ごとに情報を取得
    film_list = soup.find_all("div", class_="p-movie-cassette js-movie-cassette")

    # ページに20作品掲載してあるか確かめる(検収条件で使用)
    if len(film_list) == 20 :
        kenshu_count += 1

    for film in film_list:
        # csvファイルに出力するときに使う辞書を作成
        film_dict = {}

        # 作品数カウンタ
        film_count += 1

        # 作品名(name)
        name = film.find(class_="p-movie-cassette__title").text

        # 上映日(release_date)
        other_info = film.find(class_="p-movie-cassette__other-info")
        if "上映日" in str(other_info): #上映日が記載してある場合
            spans = film.find_all("span")
            for i in spans:
                if "年" in str(i):
                    release_date = str(i).strip("</span>")
                    if "年" and "月" and "日" in release_date :  # 上映日に"年月日"すべてが含まれている場合
                        release_date = datetime.datetime.strptime(release_date, "%Y年%m月%d日")
                    else : # "年月日"のいずれかが含まれていない場合は上映日なしとする
                        release_date = None


        else : #上映日が記載してない場合
            release_date = None

        # 上映時間(screening_time)
        other_info = film.find(class_="p-movie-cassette__other-info")
        if "上映時間" in str(other_info): #上映時間が記載してある場合
            spans = film.find_all("span")
            for i in spans:
                if "分" in str(i):
                    screening_time = str(i).strip("<分/span>")
                    screening_time = int(screening_time)


        else : #記載してない場合
            screening_time = None

        #評価(rate)
        rate = film.find(class_="c-rating__score").text
        if rate == "-": #評価がない場合
            rate = 0
        else :
            rate = float(rate)

        #視聴者数(view)
        view_ = film.find(class_="p-movie-cassette__action p-movie-cassette__action--marks")
        view = view_.find(class_="p-movie-cassette__action__body").text
        if view == "-": #評価がない場合
            view = 0
        else :
            view = int(view)

        #clip数(clip)
        clip_ = film.find(class_="p-movie-cassette__action p-movie-cassette__action--clips")
        clip = clip_.find(class_="p-movie-cassette__action__body").text
        if clip == "-": #評価がない場合
            clip = 0
        else :
            clip = int(clip)

        #全体数(total) (=視聴者数+clip数)
        total = view + clip

        #ジャンル
        #ジャンルのリスト
        genre_list = ["anime", "drama", "romance", "horror", "art", "war", "music", "musical", "sports", "SF", "youth", "comedy", "action", "adventure", "crime", "documentary", "suspence", "shortfilm",
        "family", "thriller", "zidai_geki", "fantasy", "yakuza", "mystery","biography", "western", "panic", "omnibus", "violence", "history", "gang",]
        genre_list_jp = ["アニメ", "ドラマ", "恋愛", "ホラー", "アート・コンテンポラリー", "戦争","音楽", "ミュージカル", "スポーツ", "SF", "青春", "コメディ", "アクション", "アドベンチャー・冒険", "クライム", "ドキュメンタリー", "サスペンス", "ショートフィルム・短編",
        "ファミリー", "スリラー", "時代劇", "ファンタジー", "ヤクザ・任侠", "ミステリー", "伝記", "西部劇", "パニック", "オムニバス", "バイオレンス", "ギャング・マフィア", "歴史"]
        #辞書において該当するジャンルに1,しないジャンルに0をいれる
        for genre in genre_list :       #初期値としてすべてに0をいれる
            film_dict[genre] = 0

        genre_ = film.find(class_="p-movie-cassette__genre")
        if not genre_ : # ジャンルがない場合
            pass
        else : # ジャンルがある場合
            genres = genre_.find_all("a")
            for genre in genres :
                film_dict[genre_list[genre_list_jp.index(str(genre.text))]] = 1

        #オンライン動画サービス(vod)
        #vodで見れれば1,見れなければ0
        vod = film.find(class_="p-movie-cassette__vod__title")
        if not vod : # サービスがない場合
            vod = 0
        else :
            vod = 1

        #監督(director)、脚本(screenwriter)、主演(starring)
        producer_ = film.find_all(class_="p-movie-cassette__people-list-term")
        if not producer_ : #いずれの情報もないとき
            director = None
            screenwriter = None
            starring = None

        else : # いずれかの記載がある場合
            for i in producer_:
                if i.text == "監督" : #監督が明記してある場合
                    for j in film.find_all(class_="p-movie-cassette__people-wrap") :
                        if "監督" in j.text :
                            director = j.find("a", class_="c-label").text
                elif i.text == "脚本" : # 脚本が明記してある場合
                    for j in film.find_all(class_="p-movie-cassette__people-wrap") :
                        if "脚本" in j.text :
                            screenwriter = j.find("a", class_="c-label").text
                else : # 出演者が明記してある場合
                    for j in film.find_all(class_="p-movie-cassette__people-wrap") :
                        if "出演者" in j.text :
                            starring = j.find("a", class_="c-label").text

        # csv書き出しのための辞書作り
        film_dict.update([("No.", film_count), ("name", name), ("release_date",release_date), ("screening_time",screening_time), ("rate",rate), ("view",view),
          ("clip",clip), ("total",total), ("vod",vod), ("director",director), ("screenwriter",screenwriter), ("starring",starring)])
        # csvファイルの出力
        with open("./filmarks_files/film_data.csv", "a", newline="", encoding='CP932', errors="replace") as f:
                    writer = csv.DictWriter(f, fieldnames=header)
                    writer.writerow(film_dict)

print("総ページ数：{}ページ".format(total_page))
print("{}件の作品データを取得".format(film_count))

# 検収条件の確認
if total_num == film_count :
    print("検収条件クリア")
else :
    print("取得データの方が{}件少ないです。".format(total_num - film_count))
    print("ただし、今回使用したサイトでは1ページに20作品掲載されており、最終ページも20作品掲載されています。")
    print("すなわち、今回取得したとされるデータ数は 20×{0}ページ = {1}件 と考えられます。".format(total_page, 20*total_page))
    print("実際に20作品掲載されていたページ数は{}ページです。".format(kenshu_count))
    if 20*kenshu_count == film_count and total_page == kenshu_count : # 20 × (20作品掲載されているページ数) == 取得データ件数 となる場合
        print("よって、実際にすべてのページに20作品掲載されているので、サイトに表示されていた作品件数は間違えだと考えられ、検収条件はクリアしています。")
    else :
        print("しかし、その場合でもやはり件数が一致しないので検収条件はクリアしていません。")

print("スクレイピング終了")
