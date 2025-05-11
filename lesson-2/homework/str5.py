n=input()
check="aeiuoyAEIOUY"
vowels=0
consonants=0
for i in n:
    if i in check:
        vowels+=1
    else:
        consonants+=1
print("vowels:",vowels)
print("consonants:",consonants)
