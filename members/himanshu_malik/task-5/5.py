values =  [30, 31, 33, 34, 35]

def trend_tracker(lst):

    cons_diff = 0
    avg_diff = 0
    tot_diff = 0
    trend = ''

    for i in range(1,len(lst)):
        cons_diff = lst[i]-lst[i-1]
        tot_diff += cons_diff
        avg_diff = (tot_diff+avg_diff)/i
    next_value = lst[-1]+ avg_diff

    if avg_diff>0:
        trend = "Rising"
    elif avg_diff<0:
        trend = "Falling"
    else:
        trend = "Stable"
        
    print (f"Looking at the trend, the values are {trend}")
    print (f"Predicted next value: {next_value}")

trend_tracker(values)
