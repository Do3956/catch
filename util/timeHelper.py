import time
import datetime
from time import strftime,strptime,localtime,mktime



def curDateDatabase():
    ''' get today str,date format="YYYY-MM-DD"'''
    return strftime("%Y-%m-%d", localtime())


def curdate():
    ''' get today str,date format="YYYYMMDD"'''
    return strftime("%Y%m%d", localtime())


def tomorrow(days):
    '''返回格式2014-11-27
        距离现在XX天的时间
    '''
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days)
    return tomorrow


def addHours(hour):
    '''返回格式20141127 14:43:53
    '''
    futureTS = time() + hour * 3600
    return strftime("%Y%m%d %H:%M:%S", localtime(futureTS))


def addDay(days, sTime=None):
    '''返回格式2014-11-27 14:43:53
    '''
    if sTime:
        sTS = formatTimeStamp(sTime) / 1000.0
    else:
        sTS = time()
    futureTS = sTS + days * 86400
    return strftime("%Y-%m-%d %H:%M:%S", localtime(futureTS))


def addDays(days, sTime=None):
    '''返回格式20141127 14:43:53
    '''
    if sTime:
        sTS = formatTS(sTime) / 1000.0
    else:
        sTS = time()
    futureTS = sTS + days * 86400
    return strftime("%Y%m%d %H:%M:%S", localtime(futureTS))


def curTimeInt():
    '''返回格式  时分 1443'''
    return int(strftime("%H%M", localtime()))


def curTime():
    '''返回格式  时分秒 14:43:53'''
    return strftime("%H:%M:%S", localtime())


def curDateTimeStr():
    '''返回格式20141127 14:43:53'''
    return strftime("%Y%m%d %H:%M:%S", localtime())


def curDateTime():
    '''返回格式2014-11-27 14:43:53'''
    return strftime("%Y-%m-%d %H:%M:%S", localtime())


def curTS():
    '''返回秒级的时间戳'''
    return int(round(time()))


def curTimeStamp():
    '''返回毫秒级的时间戳'''
    return int(round(time() * 1000))


def formatTS(dataTime):
    '''返回20141127 14:43:53 毫秒级的时间戳'''
    dataTime = str(dataTime)
    if '-' in dataTime:
        if len(dataTime) == 10:
            TS = int(round(mktime(strptime(dataTime, "%Y-%m-%d")) * 1000))
        else:
            TS = int(round(mktime(strptime(dataTime, "%Y-%m-%d %H:%M:%S")) * 1000))
    elif len(dataTime) == 8:
        TS = int(round(mktime(strptime(dataTime, "%Y%m%d")) * 1000))
    else:
        TS = int(round(mktime(strptime(dataTime, "%Y%m%d %H:%M:%S")) * 1000))
    return TS


def dateToDate(dateInt):
    '''将20141127转为2014-11-27'''
    ts = int(round(mktime(strptime(str(dateInt), "%Y%m%d"))))
    date = strftime("%Y-%m-%d", localtime(ts))
    return date


def DTToDT(dateInt):
    '''将20141127 14:43:53转为2014-11-27 14:43:53'''
    ts = int(round(mktime(strptime(str(dateInt), "%Y%m%d %H:%M:%S"))))
    date = strftime("%Y-%m-%d %H:%M:%S", localtime(ts))
    return date


def formatTimeStamp(dataTime):
    '''返回2014-11-27 14:43:53 毫秒级的时间戳'''
    dataTime = str(dataTime)
    try:
        TS = int(round(mktime(strptime(dataTime, "%Y-%m-%d %H:%M:%S")) * 1000))
    except:
        TS = int(round(mktime(strptime(dataTime, "%Y%m%d")) * 1000))
    return TS


def ReturnDateTime(timeStamp):
    '''将毫秒级的时间戳转为 2014-11-27 14:43:53 形式'''
    return strftime("%Y-%m-%d %H:%M:%S", localtime(timeStamp / 1000))


def getDateTime(timeStamp):
    '''将毫秒级的时间戳转为 20141127 14:43:53 形式'''
    return strftime("%Y%m%d %H:%M:%S", localtime(timeStamp / 1000))


def isToday(dateTime):
    '''判断日期是否为今天'''
    if dateTime:
        dateTime = str(dateTime)
        now = curDateTime()
        if dateTime.split(' ')[0] == now.split(' ')[0]:
            return True
    return False


def isTodayDate(date):
    '''判断日期是否为今天'''
    if date == curdate():
        return True
    return False


def isThisMonthDate(date):
    '''判断日期是否为这个月'''
    if date and date[:-2] == curdate()[:-2]:
        return True
    return False


def isTimeFree(lastDataTime, interval=0):
    '''是否已经解封
    lastDataTime 与现在的间隔是否超过 interval,毫秒级
    lastDataTime 2014-11-27 14:43:53
    '''
    if lastDataTime:
        lastTS = formatTimeStamp(lastDataTime)
        nowTS = curTimeStamp()
        if nowTS - lastTS < interval:
            return False
    return True


def isTimeStrFree(lastDataTime, interval=0, endTime=None):
    '''是否已经解封
             与现在的间隔是否超过 interval,毫秒级
    lastDataTime 20141127 14:43:53
    '''
    if endTime:
        nowTS = formatTS(endTime)
        lastTS = curTimeStamp()
        if 0 < nowTS - lastTS < interval:
            return False
        return True

    if lastDataTime:
        lastTS = formatTS(lastDataTime)
        nowTS = curTimeStamp()
        if nowTS - lastTS < interval:
            return False
    return True


def isEffectByDay(lastDataTime, day):
    '''是否在有效期中
    '''
    lastTS = formatTimeStamp(lastDataTime) + 28800000
    nowTS = curTimeStamp() + 28800000
    if nowTS / 86400000 - lastTS / 86400000 < day:
        return True
    return False


def isBetweenTime(time1, time2):
    '''是否在有效期中
    time1 时分 1120
    '''
    _now = datetime.datetime.now()
    curTime = _now.hour * 100 + _now.minute
    if time2 >= curTime >= time1:
        return True
    return False


def isBetweenDateTime(time1, time2):
    '''是否在有效期中
    time1 20151101 11:20:00
    '''
    TS1 = formatTS(time1)
    TS2 = formatTS(time2)
    if TS2 >= curTimeStamp() >= TS1:
        return True
    return False


def getDayDiff(lastDateTime, nowDateTime=None):
    '''获取现在 和  lastData 的天数差
    '''
    if nowDateTime:
        nowTS = formatTimeStamp(nowDateTime) + 28800000
    else:
        nowTS = curTimeStamp() + 28800000

    lastTS = formatTimeStamp(lastDateTime) + 28800000
    return nowTS / 86400000 - lastTS / 86400000


def isSameWeek(date1, date2=None):
    '''
    @param date1: 20151010 int
    '''
    date1 = str(date1)
    week1 = datetime.datetime(int(date1[:4]), int(date1[4:6]), int(date1[-2:])).isocalendar()[1]
    if date2:
        date2 = str(date2)
    else:
        date2 = curdate()
    week2 = datetime.datetime(int(date2[:4]), int(date2[4:6]), int(date2[-2:])).isocalendar()[1]
    #     print 'date1',date1
    #     print 'date2',date2
    #     print 'week1',week1
    #     print 'week2',week2
    if week1 == week2:
        return True
    return False


def getTodayValue(value, lastDate):
    '''查看今天的数据
    '''
    if lastDate == curdate():
        return value
    else:
        return 0


def getThisMonthValue(value, lastDate):
    '''查看本月的数据
    '''
    if isThisMonthDate(lastDate):
        return value
    else:
        return 0