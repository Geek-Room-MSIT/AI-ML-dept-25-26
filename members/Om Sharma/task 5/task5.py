values = [30, 31, 33, 34, 35]

differences = []
n = len(values)
for i in range(1,n):
    diff = values[i] - values[i-1]
    differences.append(diff)

avg_diff = sum(differences) / len(differences)

if avg_diff > 0:
    trend = "rising"
elif avg_diff < 0:
    trend = "falling"
else:
    trend = "stable"

next_value = values[-1] + avg_diff

print(f"Differences between consecutive values: {differences}")
print(f"Average difference: {avg_diff:.2f}")
print(f"Trend: {trend}")
print(f"Predicted next value: {next_value:.2f}")
