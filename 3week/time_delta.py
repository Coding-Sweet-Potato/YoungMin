# Not yet
# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
import datetime
for _ in range(int(input())):
    input_str = list(input().split())
    str_date = ' '.join(input_str[:-1])
    time_zone = input_str[-1]
    t1 = datetime.datetime.strptime(str_date,'%a %d %b %Y %H:%M:%S')
    h,m = int(time_zone[:3]),int(time_zone[-2:])
    t1 += datetime.timedelta(hours=-h,minutes = -m)
    
    
    input_str2 = list(input().split())
    str_date2 = ' '.join(input_str2[:-1])
    time_zone2 = input_str2[-1]
    t2 = datetime.datetime.strptime(str_date2,'%a %d %b %Y %H:%M:%S')
    h2,m2 = int(time_zone2[:3]),int(time_zone2[-2:])
    t2 += datetime.timedelta(hours=-h2,minutes=-m2)
        
    if t1 >= t2:
        result = t1 - t2
    else:
        result = t2-t1
    print(int(result.total_seconds()))