#Task 5: Trend Tracker
import math
num=[]
a=int(input("Enter how many numbers you want to add in list:"))
for i in range(a):
   b=int(input(f"Enter the value {i+1}:"))
   num.append(b)
trend=[]
for i in range(a-1):
    diff = num[i+1]-num[i]
    trend.append(diff)
avg_diff=sum(trend)/len(trend)
next_value=num[-1]+avg_diff
if abs(avg_diff)<0.2:
    t="stable"
elif avg_diff > 0:
    t="rising"
else:
    t="falling"
print(f"Trend detected:{t}")
print(f"Predicted next value:{next_value}")
