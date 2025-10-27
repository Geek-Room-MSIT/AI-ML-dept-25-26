#Define the list
values = [120, 131, 100, 324, 135]

#find differences between consecutive values
diffs = [values[i+1] - values[i] for i in range(len(values)-1)]

avg_diff = sum(diffs) / len(diffs)

if avg_diff > 0:
    trend = "rising"
elif avg_diff < 0:
    trend = "falling"
else:
    trend = "stable"

next_value = values[-1] + avg_diff

print(f"Trend: {trend}")
print(f"Predicted next value: {next_value:.2f}")
