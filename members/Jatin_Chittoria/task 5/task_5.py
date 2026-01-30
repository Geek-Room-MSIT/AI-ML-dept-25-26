numbers = input("Enter numbers by spaces: ")
numbers = [int(x) for x in numbers.split()]
differences = []
for i in range(1, len(numbers)):
    diff = numbers[i] - numbers[i - 1]
    differences.append(diff)
avg_diff = sum(differences) / len(differences)

if avg_diff > 0:
    trend = "Rising "
elif avg_diff < 0:
    trend = "Falling "
else:
    trend = "Stable "

next_value = numbers[-1] + avg_diff

print("\n--- Trend Tracker Results ---")
print("Numbers entered:", numbers)
print("Trend tracked:", trend)
print("Est. next value:", round(next_value, 2))
