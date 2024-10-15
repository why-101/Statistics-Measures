import matplotlib.pyplot as plt
from main import r,r1, manual_rank
import numpy as np

month = [9, 4, 7, 11, 59, 7, 8, 25, 5, -5, 27, 20, 25, 14, 37, 10, 22, 27,21, 3, 6, 10, 30, 7, 17, 40, 15, 29, 12, 35]
week_1n2 = [9, 4, 7, 11, 59, 7, 8, 25, 5, -5, 27, 20, 25, 14, 37]
week_3n4 = [10, 22, 27,21, 3, 6, 10, 30, 7, 17, 40, 15, 29, 12, 35]


print("length of data set is:", len(month))

def mean(x):
    mean = sum(x) / len(x)
    return mean
m = mean(month)
print("sample mean is:", m)

def median(x):
    m_l = sorted(x)
    if (len(x) % 2 == 0):
        i = int(len(m_l) / 2)-1
        med = (m_l[i] + m_l[i + 1]) / 2
        return med
    else:
        i = round(len(x) / 2)-1
        med = m_l[i]
        return med

med = median(month)
print("sample median is:", med)

def mode(x):
    dit = {}

    for i in (x):
        k = i
        v = x.count(i)
        dit.update({k: v})

    ix = max(dit.values())
    mode = list(filter(lambda x: dit[x] == ix, dit))
    return mode

mm = mode(month)
print("sample mode is: ", mm)

def range(x):
    mi = min(month)
    ma = max(month)
    return ma - mi

ra = range(month)
print("range of sample is: ", ra)


def IQR(x):
    r = sorted(x)
    if (len(x) % 2 == 0):
        lower = r[:len(x)//2]
        upper = r[len(x)//2:]
    else:
        lower = r[:len(x) // 2]
        upper = r[len(x) // 2+1:]

    q1 = median(lower)
    q3 = median(upper)

    I = q3 - q1

    return q1, q3, I

iq = IQR(month)
print("q3 is", iq[0], "q1 is", iq[1], ", IQR of sample data is: ", iq[2])

def percentile(x, y):
    sl = sorted(month)
    m = sl.index(x)
    percent = (m/(len(sl))) * 100
    print("percentile of given element is ",round(percent, 2))
    po = (y * (len(sl)))/100
    print("position of given percentile: ", round(po))
percentile(4,50)


def sd(x):
    me = sum(x) / len(x)
    li = []
    for i in x:
        n = i - me
        li.append(round(n, 2))
    print("Deviation of given data is: ", li)
    li1 = []
    for i in li:
        i = i**2
        li1.append(i)
    variance = sum(li1) / len(li1)
    return round(variance,2)
var = sd(month)
print("variance of given data is: ", var)
print("Standard deviation of given data is: ", round(var**0.5,2))


o = []
def out(xy):
    lv = mean(month) - var**0.5
    hv = mean(month) + var**0.5
    for x in month:
        if (x < lv):
            o.append(x)
        elif (x > hv):
            o.append(x)
        else:
            pass
out(month)
print("outliers: ", o)

plt.hist(month)
plt.show()


r(week_1n2, week_3n4)
r1(week_1n2, week_3n4)
sx = manual_rank(week_1n2)
sy = manual_rank(week_3n4)

n = []
for i, v in enumerate(sx):
    f = sy[i] - sx[i]
    n.append(f ** 2)
d = sum(n)


p = 1 - ((6*d)/(len(sx)**3-len(sx)))
print("Spearman’s rank correlation coefficient", p)

z = np.polyfit(week_1n2,week_3n4, 1)
p = np.poly1d(z)
plt.plot(week_1n2, p(week_1n2))

plt.scatter(week_1n2, week_3n4)
plt.show()
