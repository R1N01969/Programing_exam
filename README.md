# Programing_exam
Apache HTTPのアクセスログ解析用プログラムです
アクセスログはvar/log/httpd/に配置してあります．
解析用プログラムはvarと同じ階層に配置してしようします．
httpdにはアクセスファイル以外のtxtファイルはないということを前提にしています．
httpdに試験用としてapache_loggenを用いて作成した複数のアクセスログファイルを配置してあります．

analog.pyを実行すると同じ階層にanalog.csvを出力します．
csvファイルによる出力なのでMatlabやpandasなど様々な解析ソフトで開くことができます．
analog.pyには時間帯別アクセス数とリモートホストアドレス別アクセス数を集計してあります．（問1）

実行中に保持しているのはアクセスログの年月日，時間，リモートホストアドレスのみでアクセスログファイルを読み込む際も1行ずつ行っているため，
アクセスログファイルを10GBにしてもメモリ2GBで動くはずです．（問4）

# 集計ファイルの見方
---Access number about time---の後から時間帯別アクセス数の集計結果が出力されています．
Time:, 23, 11000は1列目が集計種別，2列目が時間帯，3列目がその時間帯のアクセス数を表します．

---Access number about remote host address---の後からリモートホストアドレス別アクセス数の集計結果が出力されています．
Address:, 17.0.963.56, 1615は1列目が集計種別，2列目がリモートホストアドレス，3列目がそのアドレスのアクセス数を表します．


# 使い方
python analog.py（オプション無し）でhttpd内のアクセスファイルを全てを対象に集計します．（問2）

python analog.py YYYY/MM/DD YYYY/MM/DDというように年（Y）月（M）日（D）を指定することができます．
指定することで1つ目の日付から2つ目の日付間のアクセスログを対象に集計することができます．（問3）
