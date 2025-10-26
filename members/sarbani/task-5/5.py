values = [30, 31, 33, 34, 35]
for i in range(len(values) - 1):
    x=values[i+1]-values[i]
    y=x/(len(values)-1)
if y>0:
    print("rising")
elif y<0:
    print("falling")
else:
    print("Stable")

next_value = values[-1] + y
print(next_value)