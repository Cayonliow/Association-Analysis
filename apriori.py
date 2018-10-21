import numpy as np
from pprint import pprint
class Apriori:
    def __init__(self, support_threshold, confidence_threshold):
        self.support_threshold = support_threshold 
        self.confidence_threshold = confidence_threshold

    def count(self, filename):
        self.total = 0 
        items = {}

        with open(filename) as f:
            for transaction in f:
                self.total += 1
                for i in transaction.strip().split(','):
                    if i in items:
                        items[i] += 1.
                    else:
                        items[i] = 1.
            
        self.items = {i:j/self.total for i,j in items.items() if j/self.total > self.support_threshold}
        self.item2id = {j:i for i,j in enumerate(self.items)}
        self.D = np.zeros((self.total, len(items)), dtype=bool)
        
        with open(filename) as f:
            for n,transaction in enumerate(f):
                for i in transaction.strip().split(','):
                    if i in self.items:
                        self.D[n, self.item2id[i]] = True

    def find_rules(self, filename):
        self.count(filename)
        rules = [{(i,):j for i,j in self.items.items()}]
        l = 0
        while rules[-1]:
            rules.append({})
            keys = sorted(rules[-2].keys())
#             print('keys = =',keys)
            num = len(rules[-2])
#             print(num)
#             print(len(rules))
            l += 1
            for i in range(num):
                for j in range(i+1,num):
#                     print(keys[i][:l-1],keys[j][:l-1])
                    if keys[i][:l-1] == keys[j][:l-1]:
#                         print('i', i, 'j', j, 'keys[i] + (keys[j][l-1],)', keys[i], (keys[j][l-1]), keys[j])
                        _ = keys[i] + (keys[j][l-1],)
#                         print('_=', _)
                        _id = [self.item2id[k] for k in _]
#                         print('_id = ',_id)
#                         print('self.D[:, _id] = ',self.D[:, _id])
                        support = 1. * sum(np.prod(self.D[:, _id], 1)) / self.total
                        if support > self.support_threshold:
                            rules[-1][_] = support
        
#         pprint(rules)
        result = {}
        for n,j in enumerate(rules[1:]):
            for r,v in j.items():
                for i,_ in enumerate(r): # find association rule
                    x = r[:i] + r[i+1:]
                    if v / rules[n][x] > self.confidence_threshold:
                        result[x+(r[i],)] = (v / rules[n][x], v)
#                         print(result[x+(r[i],)], (confidence, v))

        return sorted(result.items(), key=lambda x: -x[1][0])