def analyze_trend(values):
    diffs = [b - a for a, b in zip(values, values[1:])]
    avg = sum(diffs) / len(diffs)
    trend = "Rising" if avg > 0.01 else "Falling" if avg < -0.01 else "Stable"
    return trend, values[-1] + avg

def main():
    try:
        values = [30, 31, 33, 34, 35]
        trend, next_val = analyze_trend(values)
        print("Values:", values)
        print(f"Trend: {trend}")
        print(f"Predicted next value: {next_val:.2f}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
