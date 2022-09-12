import matplotlib.pyplot as plt
import re
import collections
import glob
import sys
import datetime as dt
from pathlib import Path
import os.path

#実行オプション
args = sys.argv
args_on = False
if len(args) > 1:
    from_date = dt.datetime.strptime(args[1], '%Y/%m/%d')
    to_date = dt.datetime.strptime(args[2], '%Y/%m/%d')
    args_on = True

#ログファイルのパスを指定
path_output = 'analog.csv'
flist = sorted(glob.glob('var/log/httpd/*.txt'))
time = list()
host = list()
date = list()

#ログファイルを開く
for filename in flist:
    try:
        with open(filename) as f:
            s = f.readline()
            while s:
                regex1 = re.compile('[0-9]+\/[A-Z][a-z][a-z]\/[0-9]+\:[0-9][0-9]\:[0-9][0-9]\:[0-9][0-9]')
                regex2 = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')

                match1 = regex1.findall(s)
                match2 = regex2.findall(s)
                if match1 != [] or match2 != []:
                    date.extend(match1)
                    host.extend(match2)
                s = f.readline()

    except FileExistsError:
            print('Sorry, I cant find log file.')

if args_on == True:
    for i in range(len(date)):
        date[i] = date[i].replace('Jan','1').replace('Feb','2').replace('Mar','3').replace('Apr','4').replace('May','5').replace('Jun','6').replace('Jul','7').replace('Aug','8').replace('Sep','9').replace('Oct','10').replace('Nov','11').replace('Dec','12')
        if from_date <= dt.datetime.strptime(date[i], '%d/%m/%Y:%H:%M:%S') <= to_date:
            temp = dt.datetime.strptime(date[i], '%d/%m/%Y:%H:%M:%S')
            #時間帯別アクセス回数
            time.append(str(temp.hour))
            sortime = collections.Counter(time)
            tnum, tacc = zip(*sortime.most_common())

            sorthost = collections.Counter(host)
            rnum, racc = zip(*sorthost.most_common())

        else:
            tnum = str('dont exist')
            rnum = str('dont exist')
            tacc = str('dont exist')
            racc = int('dont exist')
            print('Sorry, logs dont exist in range')
            break

else:
    for i in range(len(date)):
        if len(date) > 0:
            temp = dt.datetime.strptime(date[i], '%d/%m/%Y:%H:%M:%S')
            #時間帯別アクセス回数
            time.append(str(temp.hour))
            sortime = collections.Counter(time)
            tnum, tacc = zip(*sortime.most_common())

            sorthost = collections.Counter(host)
            rnum, racc = zip(*sorthost.most_common())

        else:
            tnum = str('dont exist')
            rnum = str('dont exist')
            tacc = str('dont exist')
            racc = int('dont exist')
            print('Sorry, logs dont exist in log files')
            break

with open(path_output, mode ='w+') as f:
    f.write('---Access number about time---\n')
    for i in range(len(tnum)):
        f.write('Time:,')
        f.write(str(tnum[i]) + ',')
        f.write(str(tacc[i]) + '\n')
    f.write('---Access number about remote host address---\n')
    for i in range(len(rnum)):
        f.write('Address:,')
        f.write(str(rnum[i]) + ',')
        f.write(str(racc[i]) + '\n')
