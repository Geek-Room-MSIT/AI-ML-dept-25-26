#Given a list of numbers (like daily temperatures or stock prices), detect if the trend is rising, falling, or stable — and estimate the next value.

def temp_predict(temp):
    i=1
    temp_diff=[]
    while i <= len(temp)-1:
        a = temp[i]-temp[i-1]
        temp_diff.append(a)
        i=i+1
    avg_diff = sum(temp_diff)/len(temp)
    print(f"Average temperature difference : {avg_diff}")
    if avg_diff>0:
        print("The temperature is rising")
    elif avg_diff<0:
        print("The temperature is falling")
    else:
        print("The temperature is stable")
    next_temp = temp[-1] + avg_diff 
    print(f"Predicted next value: {next_temp}")


temp = [31,31,29,28,30,31,29]    
temp_predict(temp)