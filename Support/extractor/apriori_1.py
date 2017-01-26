__author__ = 'ZEUS'

def load_dataset():
    print("=====Method for loading the data set=====")
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5], [2,6]]

def createCl(dataset):
    print("====Create a list of candidate item sets of size ONE ====")
    "Create a list of candidate item sets of size ONE"
    cl = []
    for transaction in dataset:
        for item in transaction:
            if not[item] in cl:
                cl.append([item])
    cl.sort()
    "frozen set becuse it will kind of a dictionary"
    return map(frozenset,cl)

def scanD(dataset,candidates,min_support):
    print("=======returns all candidates that meets a minimum support level=======")
    "returns all candidates that meets a minimum support level"
    sscnt = {}
    for tid in dataset:
        for can in candidates:
            if can.issubset(tid):
                sscnt.setdefault(can,0)
                sscnt[can] +=1

    num_items = float(len(dataset))
    retlist = []
    support_data = {}
    for key in sscnt:
        support = sscnt[key]/num_items
        if support >= min_support:
            retlist.insert(0,key)
            support_data[key] = support
    return retlist,support_data

def aprioriGen(freq_sets ,k):
    print("=====Generate the joint transaction from candidate sets=======")
    "Generate the joint transaction from candidate sets"
    reList = []
    lenLk = len(freq_sets)
    for i in range(lenLk):
        for j in range(i + 1,lenLk):
            L1 = list(freq_sets[i])[:k - 2]
            L2 = list(freq_sets[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                reList.append(freq_sets[i] | freq_sets[j])
    return reList

def apriori(dataset, minsupport=0.5):
    print("========Generate a list of candidate item sets========")
    "Generate a list of candidate item sets"
    C1 = createCl(dataset)
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

def generateRules(L,support_data,min_confidence=0.7):
    "Create the association rules"
    " L: list of frequent item sets"
    "support_data : support data for those item sets"
    "min confidence : minimum confidence threshold"
    rules = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            print "freqSet", freqSet, 'H1', H1
            print("\n")
            print("\n")
            print("\n")
            if (i > 1):
                rules_from_conseq(freqSet, H1, support_data, rules, min_confidence)
            else:
                calc_confidence(freqSet, H1, support_data, rules, min_confidence)
    return rules

def calc_confidence(freqSet, H, support_data, rules, min_confidence=0.7):
    "Evaluate the rule generated"
    pruned_H = []
    for conseq in H:
        conf = support_data[freqSet] / support_data[freqSet - conseq]
        if conf >= min_confidence:
            print freqSet - conseq, '--->', conseq, 'conf:', conf
            rules.append((freqSet - conseq, conseq, conf))
            pruned_H.append(conseq)
    return pruned_H

def rules_from_conseq(freqSet, H, support_data, rules, min_confidence=0.7):
    "Generate a set of candidate rules"
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calc_confidence(freqSet, Hmp1,  support_data, rules, min_confidence)
        if len(Hmp1) > 1:
            rules_from_conseq(freqSet, Hmp1, support_data, rules, min_confidence)

#**********************************************************************
#***************************************************************************************
#****************************************************************************************************
