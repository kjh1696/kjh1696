

eyes_right = float(input())
eyes_left = float(input())

if eyes_right >= 1.0 and eyes_left >= 1.0:
    print(f"High")
elif eyes_right >= 0.5 and eyes_left >= 0.5:
    print(f"Middle")
else:
    print(f"Low")