try:
    chensage = int(input("陳斌幾歲：   "))
    print("無、被閹割、有對象、意外身亡、截肢")
    chensstate = input("陳斌的狀態是哪個  ")
except:
    raise ValueError("請重開並輸入一次資料")

if chensage >= 0 and chensage < 1:
    chensage = "斌斌mini v1"
elif chensage >= 1 and chensage <6:
    chensage = "斌斌 mini v2"
elif chensage >= 6 and chensage <12:
    chensage = "小斌斌"
elif chensage >= 12 and chensage <15:
    chensage = "斌斌"
elif chensage >= 15 and chensage < 18:
    chensage = "大斌斌"
elif chensage >= 18 and chensage < 22:
    chensage = "斌斌 Plus"
elif chensage >= 22 and chensage <45:
    chensage = "斌斌Pro"
elif chensage > 65 and chensage < 100:
    chensage = "斌斌 Pro Max"
elif chensage > 100:
    chensage = "陳公斌斌"
else:
    raise ValueError("請重開並輸入一次資料")

if chensstate == "無":
    finalchen = chensage
elif chensstate == "被閹割":
    finalchen = "1/2"+chensage+"(閹)"
elif chensstate == "有對象":
    sex = input("對象的性別：   ")
    finalchen = chensage+"("+sex+")"
elif chensstate == "意外身亡":
    finalchen = "Ex."+chensage
elif chensstate == "截肢":
    cuted = input("被截肢的比例：   ")
    finalchen = cuted+chensage+"(截)"
else:
    raise ValueError("請重開並輸入一次資料")

print(finalchen)