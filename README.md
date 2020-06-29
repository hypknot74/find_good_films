# find_good_films
高評価かつ多くの人から見られている映画の見つけ方を約3万件の作品データから分析

## 概要
「**多くの人が観ており、かつ満足できる、コスパの良い作品選びをするための手順を提案する。**」\
を目標としてデータ分析を行いました。
以下で具体的な方法と結果を示します。

## 目次

## 内容
### 1. テーマ
現在、コロナウイルスの影響で外出を控えなければなりません。こんなときこそ家で映画を観るチャンスであり、なるべく多くの人と共通の話題となる映画作品を観ておきたいと考えました。今回は、\
「多くの人が観ており、かつ満足できる、コスパの良い作品選びをするための手順の提案」\
を目標とします。
※コスパの良い作品とは評価と視聴者数がともに高い作品と定義します。\
※対象作品はアメリカ映画のみとします。

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

![re_film](https://github.com/hypknot74/find_good_films/blob/master/re_film.png)

### 3. データ収集
フィルマークスという日本最大級の映画レビューサイトを対象にスクレイピングして変数を得ました。**(データ取得日：2020-04-01)**\
変数として、作品名、上映日、上映時間、評価、観た人数、観る予定の人数、その総数、ジャンル、vod対応しているかしていないか、監督、脚本家、主演を取りました。\
このサイトでは評価は0.1点刻み、１〜５点で評価できます。

![web_site_ex](https://github.com/hypknot74/find_good_films/blob/master/web_site_ex.png)

![variables](https://github.com/hypknot74/find_good_films/blob/master/variables.png)

### 4. データ分析
まず最初にデータを見ます。今回、観た人数と観る予定の人数を合わせた総数を視聴者数としました。\
評価されていない作品は比較することができず、vod対応していないと外に見に行かなければならないので設定にあっていないため、評価がない作品、vod対応していない作品を除いた作品を基本データとしました。\
![base_data](https://github.com/hypknot74/find_good_films/blob/master/base_data.png)

上映時間、評価、上映日と視聴者数の関係を見ます。\
視聴者数が10万人を超える条件は
- 上映時間：80〜200分
- 評価：3.3以上4.5以下
- 上映日：1985年以降
とわかります。
![analysis1](https://github.com/hypknot74/find_good_films/blob/master/analysis.png)

ジャンルの分布です。\
３０あるジャンルから右上に位置する１１このジャンルは評価平均、視聴者平均が高いジャンルである、すなわちコスパの高い作品の割合が大きいジャンルだと考えられます。\
![analysis2](https://github.com/hypknot74/find_good_films/blob/master/analysis2.png)

左の円グラフはジャンル別に作品数の割合を示しています。\
右はジャンルごとの箱ひげ図です。下から出ている水色の棒グラフはそれぞれのジャンルの作品数を表しています。右にいくにつれて作品数の多いジャンルであることがわかります。\
ジャンル名がオレンジになっているのは先程示したコスパの高い11このジャンルです。\
赤で囲まれた箱ひげは図の上側に位置しており、作品数もそれほど多くないことから、上質な作品に出会いやすいジャンルであることがわかります。\
![analysis3](https://github.com/hypknot74/find_good_films/blob/master/analysis3.png)

監督、脚本家、主演別の分布です。\
この分布は評価平均と視聴者数平均がある一定以上の数値の人物だけを残しています。\
つまり、コスパの良い作品に多く関わっている人物のみを示したものです。\
![analysis4](https://github.com/hypknot74/find_good_films/blob/master/analysis4.png)
![analysis5](https://github.com/hypknot74/find_good_films/blob/master/analysis5.png)


