values = [30, 31, 33, 34, 35]

differences = [values[i+1] - values[i] for i in range(len(values) - 1)]
avg_diff = sum(differences) / len(differences)

if avg_diff > 0:
    trend = "rising"
elif avg_diff < 0:
    trend = "falling"
else:
    trend = "stable"

next_value = values[-1] + avg_diff

print(f"Trend: {trend}")
print(f"Predicted next value: {next_value:.2f}")
