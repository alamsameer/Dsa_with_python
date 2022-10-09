def romanToInt( s: str) -> int:
    intialValue={'I':1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XC":90,
        "C":100,
        "XD":400,
        "D":500,
        "CM":900,
        "M":1000
    }
    res=0
    i=0
    while i<len(s):
        checkKey=s[i]
        if i+1<len(s):
            print(intialValue[checkKey]<intialValue[s[i+1]])
            if intialValue[checkKey]<intialValue[s[i+1]]:
               res=res-intialValue[checkKey]
               i+=1
            else:
                res+=intialValue[checkKey]
                i+=1
        else:
            res+=intialValue[checkKey]
            i+=1
    return res


print('romanToInt("XXIV"): ', romanToInt("XXIV"))


print('romanToInt("XXV"): ', romanToInt("XCIV"))
