def calendar(n):
    DAYS_IN_400YEARS = 400*365 + 400//4 - 400//100 + 1
    DAYS_IN_100YEARS = 100*365 + 100//4 - 1
    DAYS_IN_4YEARS = 4*365 + 1
    MONTHS = [31,28,31,30,31,30,31,31,30,31,30,31]
    minute = n%60
    n //= 60
    hour = n%24
    n //= 24
    year = n//DAYS_IN_400YEARS*400
    n %= DAYS_IN_400YEARS
    year += n//DAYS_IN_100YEARS*100
    n %= DAYS_IN_100YEARS
    year += n//DAYS_IN_4YEARS*4
    n %= DAYS_IN_4YEARS
    year += n//365
    n %= 365


    if (year%4 == 0 and year%100!=0) or year%400==0:
        MONTHS[1] = 29
    
    for i in range(12):
        if n < MONTHS[i]:
            break
        n -= MONTHS[i]

    month = i+1
    day = n

    return minute,hour,day,month,year

