from collections import defaultdict

asupId = '2015012500001234'
cifsKeys = {}
shares = {}
all_counts = defaultdict(int)

all_counts['c1'] = 10
all_counts['c2'] = 20
if asupId not in cifsKeys:
    cifsKeys[asupId] = {}
    cifsKeys[asupId]['shares'] = shares
    cifsKeys[asupId]['all_counts'] = all_counts
    print cifsKeys
