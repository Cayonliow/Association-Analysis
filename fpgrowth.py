import itertools
import numpy as np
from pprint import pprint

class FPNode(object):
    def __init__(self, value, count, parent):
        self.value = value
        self.count = count
        self.parent = parent
        self.children = []
        self.link = None
        
    def has_child(self, value):
        for node in self.children:
            if node.value == value:
                return True
        return False

    def get_child(self, value):
        for node in self.children:
            if node.value == value:
                return node
        return None

    def add_child(self, value):
        child = FPNode(value, 1, self)
        self.children.append(child)
        return child
        
class FPTree(object):
    def __init__(self, transactions, minimum_support_threshold, root_value = None, root_count = None):
        self.frequent_itemset = self.find_frequent_items(transactions, minimum_support_threshold)
        self.headers = self.build_header_table(self.frequent_itemset)
        self.root = self.build_fptree(transactions, root_value,root_count, self.frequent_itemset, self.headers)
        
#         return self.frequent_itemset, self.headers, self.root

    def find_frequent_items(self, transactions, minimum_support_threshold):
        items = {}
        remaining = {}
        for transaction in transactions:
            for i in transaction:
                if i in items:
                    items[i] += 1
                else:
                    items[i] = 1
                
        for key in list(items.keys()):
            if items[key] >= minimum_support_threshold:
                remaining[key] = items[key]
        return remaining

    def build_header_table(self, frequent_itemset):
        headers = {}
        for i in frequent_itemset.keys():
            headers[i] = None
        return headers

    def build_fptree(self, transactions, root_value, root_count, frequent_itemset, headers):
        root_node = FPNode(root_value, root_count, None)
        sorted_items = []
        for trans in transactions:
            # filter out the frequent item from the transaction
            sorted_items = [x for x in trans if x in frequent_itemset]
            # sort descendingly according to the frequency of apprearance of the item 
            sorted_items.sort(key=lambda x: frequent_itemset[x], reverse=True)
            # if there frequent item in the transaction, insert to the tree
            if len(sorted_items) > 0:
                self.insert_tree(sorted_items, root_node, headers)
        return root_node

    def insert_tree(self, items, node, headers):
        first = items[0]
        remaining = items[1:]
        child = node.get_child(first)
        if child is not None:
            child.count += 1
        else:
            child = node.add_child(first)

            if headers[first] is None:
                headers[first] = child
            else:
                current = headers[first]
                while current.link is not None:
                    current = current.link
                current.link = child

        if len(remaining) > 0:
            self.insert_tree(remaining, child, headers)

    def single_path(self, node):
        num_children = len(node.children)
        if num_children > 1:
            return False
        elif num_children == 0:
            return True
        else:
            return True and self.single_path(node.children[0])

    def collect_patterns(self, threshold):
        if self.single_path(self.root):
            return self.generate_pattern_list()
        else:
            return self.zip_patterns(self.gen_sub_trees(threshold))

    def zip_patterns(self, patterns):
#         pprint(patterns)
        if self.root.value is not None:
            new_patterns = {}
            for key in patterns.keys():
                new_patterns[tuple(sorted(list(key) + [self.root.value]))] = patterns[key]
#                 print('sorted(list(key))', sorted(list(key)),'self.root.value', self.root.value,'tuple(sorted(list(key) + [self.root.value]))',  tuple(sorted(list(key) + [self.root.value])), 'key',key)
            return new_patterns
        return patterns # fptree but not subconditionalfptree

    def gen_sub_trees(self, support_threshold):
        patterns = {}
        order = sorted(self.frequent_itemset.keys(), key=lambda x: self.frequent_itemset[x])

        for item in order:
            suffixes = []
            conditional_tree = []
            node = self.headers[item]

            while node is not None:
                suffixes.append(node)
                node = node.link

            for s in suffixes:
                path = []
                parent = s.parent
                while parent.parent is not None:
                    path.append(parent.value)
                    parent = parent.parent
                for i in range(s.count):
                    if len(path)>0:
                        conditional_tree.append(path)
#                 print('conditional tree')
#                 pprint(conditional_tree)
#                 print('end_ofconditional tree')
            subtree = FPTree(conditional_tree, support_threshold, item, self.frequent_itemset[item])
            subtree_patterns = subtree.collect_patterns(support_threshold)

            for pattern in subtree_patterns.keys():
                if pattern in patterns:
                    patterns[pattern] += subtree_patterns[pattern]
                else:
                    patterns[pattern] = subtree_patterns[pattern]
        return patterns
    
    def generate_pattern_list(self):
        patterns = {}
        items = self.frequent_itemset.keys()

        if self.root.value is None:
            suffix_value = []
        else:
            suffix_value = [self.root.value]
            patterns[tuple(suffix_value)] = self.root.count

        for i in range(1, len(items) + 1):
            for subset in itertools.combinations(items, i):
#                 print('subset',subset)
                pattern = tuple(sorted(list(subset) + suffix_value))
#                 print('pattern', pattern)
                patterns[pattern] =\
                    min([self.frequent_itemset[x] for x in subset])
#                 print(min([self.frequent_itemset[x] for x in subset]))
#                 print('patterns',patterns)
#         print(patterns)
        return patterns

def find_frequent_patterns(transactions, support_count):
    tree = FPTree(transactions, support_count)
    return tree.collect_patterns(support_count)
    
def generate_association_rules(patterns, confidence_threshold, total):
    rules = {}   
    c=0
    for itemset in patterns.keys():
     
        upper_support = patterns[itemset]
        for i in range(1, len(itemset)):
            for antecedent in itertools.combinations(itemset, i):
                antecedent = tuple(sorted(antecedent))
                consequent = tuple(sorted(set(itemset) - set(antecedent)))

                if antecedent in patterns:
                    lower_support = patterns[antecedent]
                    confidence = float(upper_support) / lower_support
                    support = float(upper_support) / total

                    if confidence >= confidence_threshold:
                        rules[c] = (antecedent, consequent, confidence, support)
                        c+=1
    return rules
    
def fpgrowth(transactions, support_count, confidence, total_item):
    patterns = find_frequent_patterns(transactions, support_count)
    return generate_association_rules(patterns, confidence, total_item)