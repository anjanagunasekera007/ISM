from collections import defaultdict

for i in xrange(1, 10, 2):
    print(i)


ggggg = [["A","B","C"],["A"],["B"],["C","D"],["A","B","D"],["A","B","E"],["A","B","C"],["A","B","C","D","E"]]
results = []

mine_rec()

print ("ahaaaaaaa")
def mine_rec(patt, mdb):
    results.append((patt, len(mdb)))
    occurs = defaultdict(list)
    for (i, startpos) in mdb:
        seq = ggggg[i]
        print seq
        print " working "
        for j in xrange(startpos, len(seq)):
            l = occurs[seq[j]]
            print l
            print "DONE"