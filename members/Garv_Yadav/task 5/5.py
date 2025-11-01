values = [42, 45, 47, 50, 54, 59]

diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
avg_diff = sum(diffs) / len(diffs)
next_value = values[-1] + avg_diff

if avg_diff > 0:
    trend = "Rising"
elif avg_diff < 0:
    trend = "Falling"
else:
    trend = "Stable"

print(f"Values: {values}")
print(f"Differences: {diffs}")
print(f"Average Difference: {avg_diff:.2f}")
print(f"Trend: {trend}")
print(f"Predicted next value: {next_value:.2f}")
