import time
import csv
import sys

def load_dataset():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createC1(dataset):
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    for i in c1:
        print i
    # sys.exit(99)
    #frozenset because it will be a ket of a dictionary.
    return map(frozenset, c1)


def scanD(dataset, candidates, min_support):
    sscnt = {}
    for tid in dataset:
        for can in candidates:
            if can.issubset(tid):
                sscnt.setdefault(can, 0)
                sscnt[can] += 1

    num_items = float(len(dataset))
    retlist = []
    support_data = {}
    for key in sscnt:
        support = sscnt[key] / num_items
        if support >= min_support:
            retlist.insert(0, key)
        support_data[key] = support
    for i in sscnt:
        print i
    sys.exit(89)
    return retlist, support_data


def aprioriGen(freq_sets, k):
    retList = []
    lenLk = len(freq_sets)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(freq_sets[i])[:k - 2]
            L2 = list(freq_sets[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(freq_sets[i] | freq_sets[j])
    return retList


def apriori(dataset, minsupport=0.5):
    C1 = createC1(dataset)
    D = map(set, dataset)
    L1, support_data = scanD(D, C1, minsupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minsupport)
        support_data.update(supK)
        L.append(Lk)
        k += 1

    return L, support_data

print "BEGGGGIINGGg"
print "create dataset"
dataset = load_dataset()
print "candidateitem list "
c1 = createC1(dataset)
d = map(set,dataset)
L1,support_data = scanD(d,c1,0.5)
print "L1"
print L1
print " l1 " + str(len(L1))
L = apriori(dataset)
time.sleep(2)
print "--------------------------------  -----------------------------------"
print L
print "================================  =================================="
L,support_data = apriori(dataset,minsupport=0.5)
time.sleep(2)
print " FINAL RULES : "
print L
print type(L)
print " OWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
