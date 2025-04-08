arr = input().split()

summation = 0
count = 0
for i in arr:
    
    if int(i) >= 250:
         print(f"{summation} {summation/count :.1f}", end = "")
         break

    count = count + 1
    summation = summation + int(i)


    if count == 10:
        print(f"{summation} {summation/count :.1f}", end = "")
        break