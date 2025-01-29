import numpy as n
import matplotlib.pyplot as plt

# Get scaled ionospheric parameters using this web site:
# pick your digisonde (e.g., Lualualei)
# pick start and stop date
# https://giro.uml.edu/didbase/scaled.php
# save output to text file:
f=open("LL721fof2","r")
l=f.readlines()
dts=[]
score=[]
fof2=[]
# parse through the text file
for li in l:
    if li[0] == "#":
        print(li)
        continue
    print(li)
    row=li.split()
    dt=n.datetime64(row[0])
    print(dt)
    print(row)
    sc=float(row[1])
    freq=float(row[2])
    print(dt)
    print(sc)
    print(freq)
    dts.append(dt)
    score.append(sc)
    fof2.append(freq)

dts=n.array(dts)
score=n.array(score)
fof2=n.array(fof2)
# use only measurements with a good score

good_idx=n.where(score>80)[0]
plt.plot(dts[good_idx],fof2[good_idx],".")
plt.title("Lualualei digisonde foF2")
plt.ylabel("foF2")
plt.xlabel("Date (UT)")
plt.show()

plt.plot(dts,score,".")

plt.show()

