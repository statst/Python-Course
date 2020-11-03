strr = 'aaabbbcccdddoooo';
#strr = 'aaabbbcccdddooooo'
listt={};#frequency
s=list(strr)
print(s)

for i in range(0,len(s)):
    if s[i] in listt:
        listt[s[i]] = listt[s[i]]+1
    else:
        listt[s[i]]=1

freq=list(listt.values())
freqq={}


for i in freq:
    # print(str(i))
    if i in freqq.keys():
        freqq[i] = freqq[i]+1
    else:
        freqq[i] = 1

v=sorted(list(freqq.values()))

if len(freqq.keys()) == 1:
    print('YES')
elif len(freqq.keys()) >2:
    print('NO')
elif len(freqq.keys()) == 2 and (int(list(list(freqq.keys()))[list(freqq.values()).index(v[0])]) - int(list(list(freqq.keys()))[list(freqq.values()).index(v[1])])) == 1:
    print('YES')
else:
    print('NO')

print(freqq)
