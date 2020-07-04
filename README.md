# find_good_films
高評価かつ多くの人から見られている映画の見つけ方を約3万件の作品データから分析

## 概要
「**多くの人が観ており、かつ満足できる、コスパの良い作品選びをするための手順を提案する。**」\
を目標としてデータ分析を行いました。
以下で具体的な方法と結果を示します。

## 実施日
2020-04-01

## 内容
### 1. テーマ
コロナウイルスの影響で外出を控えなければなりません。こんなときこそ家で映画を観るチャンスであり、なるべく多くの人と共通の話題となる映画作品を観ておきたいと考えました。\
今回は\
「多くの人が観ており、かつ満足できる、コスパの良い作品選びをするための手順の提案」\
を目標とします。\
※コスパの良い作品とは評価と視聴者数がともに高い作品と定義\
※対象作品はアメリカ映画のみ

### 2. 結果
映画作品選びの手順を提案する上で重要視した指標は以下の6つです。
- 上映時間
- 上映日
- ジャンル
- 監督
- 脚本家
- 主演

この指標を踏まえて、提案するコスパの良い映画を観るための手順が下の図です。


![Proposal_Procedure](https://github.com/hypknot74/find_good_films/blob/master/Proposal_Procedure.png)


この手順で出会える映画が下の図に載っています。\
今後出てくる映画でもこの手順に該当すればコスパの良い作品だと予想されます。


![re_film](https://github.com/hypknot74/find_good_films/blob/master/re_film.png)


### 3. データ収集
フィルマークスという日本最大級の映画レビューサイトを対象にスクレイピングして変数を得ました。**(データ取得日：2020-04-01)**\
変数として、作品名、上映日、上映時間、評価、観た人数、観る予定の人数、その総数、ジャンル、vod対応しているかしていないか、監督、脚本家、主演を取りました。\
このサイトでは評価は0.1点刻み、１〜５点で評価できます。\
↓赤で囲まれた箇所を変数として取った

![web_site_ex](https://github.com/hypknot74/find_good_films/blob/master/web_site_ex.png)


↓上のページから取れた変数の表


![variables](https://github.com/hypknot74/find_good_films/blob/master/variables.png)


### 4. データ分析
まず最初にデータを見ます。今回、観た人数と観る予定の人数を合わせた総数を視聴者数としました。\
評価されていない作品は比較することができず、vod対応していないと外に見に行かなければならないので設定にあっていないと考え、評価がない作品、vod対応していない作品を除いた作品を基本データとしました。


![base_data](https://github.com/hypknot74/find_good_films/blob/master/base_data.png)



上映時間、評価、上映日と視聴者数の関係を見ます。\
視聴者数が10万人を超える条件は
- 上映時間：80〜200分
- 評価：3.3以上4.5以下
- 上映日：1985年以降

とわかりました。


![analysis1](https://github.com/hypknot74/find_good_films/blob/master/analysis.png)



次はジャンルの分布です。\
３０あるジャンルから右上に位置する１１このジャンルは評価平均、視聴者平均が高いジャンルである、すなわちコスパの高い作品の割合が大きいジャンルだと考えられます。


![analysis2](https://github.com/hypknot74/find_good_films/blob/master/analysis2.png)


さらに詳しく見ます。\
左の円グラフはジャンル別に作品数の割合を示しています。\
右はジャンルごとの箱ひげ図です。下から出ている水色の棒グラフはそれぞれのジャンルの作品数を表しています。右にいくにつれて作品数の多いジャンルであることがわかります。\
ジャンル名がオレンジになっているのは先程示したコスパの高い11このジャンルです。\
赤で囲まれた箱ひげは図の上側に位置しており、作品数もそれほど多くないことから、上質な作品に出会いやすいジャンルであることがわかります。


![analysis3](https://github.com/hypknot74/find_good_films/blob/master/analysis3.png)



監督、脚本家、主演別の分布です。\
この分布は評価平均と視聴者数平均がある一定以上の数値の人物だけを残しています。\
つまり、コスパの良い作品に多く関わっている人物のみを示したものです。


![analysis4](https://github.com/hypknot74/find_good_films/blob/master/analysis4.png)
![analysis5](https://github.com/hypknot74/find_good_films/blob/master/analysis5.png)
![analysis6](https://github.com/hypknot74/find_good_films/blob/master/analysis6.png)



以上を踏まえて、良い作品を絞り込むために初期条件としてこれらを用いることにしました。


![analysis7](https://github.com/hypknot74/find_good_films/blob/master/analysis7.png)



その結果得られたのが次の作品分布です。\
上の作品分布は絞り込んだものから評価が３．８以上で視聴者数が１０万人以上のものを載せています。


![analysis8](https://github.com/hypknot74/find_good_films/blob/master/analysis8.png)



そこから外れたものが下の表にまとめられています。


![analysis9](https://github.com/hypknot74/find_good_films/blob/master/analysis9.png)



次に、上の作品分布に載っている作品のみを出すために削除しなければならない項目や、実際には必要なかった項目を条件からなくします。\
棒線が引かれた項目が削除する必要があった、もしくは実際は不要だった項目です。


![analysis10](https://github.com/hypknot74/find_good_films/blob/master/analysis10.png)



これらを除いた結果、変更された条件です。


![analysis11](https://github.com/hypknot74/find_good_films/blob/master/analysis11.png)



変更後のデータがこちらです。\
赤色のマークの項目が変更によって削除され、青色のマークのものが残る項目です。\
変更後は、評価平均、視聴者数平均ともに増加していることがわかり、より良い絞り込み条件になっていることがわかります。


![analysis12](https://github.com/hypknot74/find_good_films/blob/master/analysis12.png)



また、全体のデータをみると、最初約３万件あった作品が３２件まで絞れ、評価、視聴者数の平均もかなり増えています。\
標準偏差はかなり小さくなったことから作品の質のぶれも抑えられたことがわかります。


![analysis13](https://github.com/hypknot74/find_good_films/blob/master/analysis13.png)



### 5. まとめ
コスパの良い映画を観るための手順を再掲します。


![Proposal_Procedure](https://github.com/hypknot74/find_good_films/blob/master/Proposal_Procedure.png)



### 6. おまけ
最後におまけとして、最初の約３万件の作品から評価が３．８以上、視聴者数が１０万人以上の作品をすべて載せた作品分布を取りました。\
これをみると、この９２作品のうち、３２作品が今回の手順で出会える作品です。\
またこの分布のなかでも右上にある、かなりコスパの高い作品２０作品のうち１１作品に出会うことができます。\
このことからも今回提案した手順が良いものであると考えられます。\
また、極めてコスパの高い作品にはラ・ラ・ランド、グレイテスト・ショーマン、ボヘミアン・ラプソディ、セッション、美女と野獣などのミュージック・ミュージカル映画が多いということがわかりました。


![analysis14](https://github.com/hypknot74/find_good_films/blob/master/analysis14.png)


## 補足
webサイトからの情報抽出について、[クローリング](https://github.com/hypknot74/find_good_films/blob/master/crawling.py)と[スクレイピング](https://github.com/hypknot74/find_good_films/blob/master/scraping.py)は別で行いました。\
クローリングしたのが2020-04-01のため、情報は若干古いかもしれないです。\
分析に関してはpandasを利用してデータの整理などをしました。図表はMatplotlibで作成しました。


## 個人的な意見
「コスパの良い作品」というフレーズを使っていますが、「評価と視聴者数がともに高い作品」は冗長だったので便宜的に使いました。\
観る映画をコスパで決めるという考え方は好きじゃないですが、そういうのもありだと思います。\
↓My Filmraks Account

<img src="https://github.com/hypknot74/find_good_films/blob/master/Filmarks_my_account.JPG" width="320px">
