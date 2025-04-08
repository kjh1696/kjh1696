n = int(input())
arr = list(map(float, input().split()))

val = sum(arr) / n

if val >= 4.0:
    print(f"{sum(arr)/n:.1f}")

    print(f"Perfect")
elif val >= 3.0:
    print(f"{sum(arr)/n:.1f}")

    print(f"Good")
else:
    print(f"{sum(arr)/n:.1f}")

    print(f"Poor")

