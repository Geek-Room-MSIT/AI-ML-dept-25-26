values = [23, 25, 28, 30, 27]
sum_of_diff=0

for i in range(1,len(values)):
    diff=values[i]-values[i-1]
    sum_of_diff+=diff
    
avg_diff=sum_of_diff/(len(values)-1)

if avg_diff>0:
    print("Rising")
elif avg_diff<0:
    print("Falling")
else:
    print("Stable")
    
next_value=values[-1]+avg_diff
print(f"Predicted next value: {next_value}")