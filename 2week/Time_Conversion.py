# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def timeConversion(s):
    
    in_time = datetime.strptime(s, "%I:%M:%S%p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    return out_time
  
