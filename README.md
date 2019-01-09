# Data Mining Homework1 - Association Analysis
###### tags: `datamining`
---


[TOC]

## Dataset
### IBM Quest Synthetic Data Generator
*    parameter:
        *    `ntrans`, number of transaction = 1(*1000)
        *    `tlen`, average length per transaction = 10
        *    `nitems`, number of types of item = 1(*1000)
        *    `npats`, number of pattern = 100

**minimum support = 0.1(98 instances)**
**minimum confidence = 0.9**
>according to the result of WEKA

```
IBM Quest Data Generator.exe" lit -ntrans 1 -tlen 10 -nitems 1 -npats 100 -fname test
```

### Kaggle dataset: [Association of shopping basket](https://www.kaggle.com/lalalalsa/association-of-shopping-basket/data)
* The data records the time and id of an item to be bought
* the original data format has 3 columns
    * `date`
    * `id`
    * `item`
* it is manually be transformed to the format used by the process
* each transaction represents items bought per times

* parameter:
    * `ntrans`, number of transaction = 1(*1000)
    * `tlen`, average length per transaction = 10
    * `nitems`, number of types of item = 1(*1000)
    * `npats`, number of pattern = 100

**minimum support = 0.1(98 instances)**
**minimum confidence = 0.9**
>according to the result of WEKA
```
IBM Quest Data Generator.exe" lit -ntrans 1 -tlen 10 -nitems 1 -npats 100 -fname test
```

## Implemantation 
### Apriori Algorithm
the algorithm are practiced with `Class` in `apriori.py` and be furthered imported by `main.py`

It is also be visualized by part and explained in `apriori.ipynb`
#### Component
* support_threshold
* confidence_threshold
* total = total transactions

#### Function 
* `count(items)`
    * count the number of appearance of item in every transaction
* `find_rules(filename)`
    * find out the association rule of the transaction

### FP-Growth Algorithm
the algorithm are practiced with `Class` in `fpgrowth.py` and be furthered imported by `main.py`
It is also be visualized by part and explained in `fpgrowth.ipynb`
#### Nodes generation in the frequent pattern tree
* component in a node:
    * `value` = the numeric value of the node
    * `count` = number of appearance of the the element in all the transactions
    * `parent` = upper node connected
    * `children` = lower node connected
    * `link` = which to link

* function of each node
    * `has_child(value)`
        * return True if the node to check is in its children list
    * `get_child(value)`
        * return the children list of the node
    * `add_child(value)`
        * add the new node to the children list and return its position in the children list


#### Frequent pattern tree generation 
##### component
* frequent itemset
* header
* root = NULL

##### function 
###### build the FP-tree
* `find_frequent_items(transactions, minimum_support_threshold)`
    * count the number of every item appears in every transaction
* `build_header_table(frequent_itemset)`
    * initialize header table
* `build_fptree(transactions, frequent, headers)`
    * build the fp-tree and return theroot node
* `insert_tree(items, node, headers)`
    * add the frequent item list to the tree
    
###### build the fp cond. tree and generate the pattern
* `collect_patterns(threshold)`
    * generate all the possible patterns and collect it  
* `single_path(node)`
    * check whether the sub cond. fpftree is having only the single path
* `zip_patterns(patterns)`
* `gen_sub_trees(threshold)`
    * generate sub. conditional fp-tree
* `generate_pattern_list():`
    * the final step of getting the frequent pattern list

## Implementation of IBM Quest Synthetic Data Generator Dataset
### result of Apriori Algorithm
#### result from WEKA
![](https://i.imgur.com/6a7jcNn.png =300x)

#### result from implementation
```
Rule  1   ('472', '885')  ->  732  confidence: 94 % support: 0.10838
Rule  2   ('472', '833')  ->  732  confidence: 94 % support: 0.10327
Rule  3   ('732', '833')  ->  472  confidence: 93 % support: 0.10327
Rule  4   ('833', '885')  ->  732  confidence: 93 % support: 0.10123
Rule  5   ('732', '885')  ->  472  confidence: 92 % support: 0.10838
Rule  6   ('472', '737')  ->  732  confidence: 92 % support: 0.10634
Rule  7   ('472', '885')  ->  737  confidence: 91 % support: 0.10532
```

### result of Fp-growth
#### result from WEKA
![](https://i.imgur.com/RFbK53i.png =300x)

#### result from implementation
```
Rule  1   ('472', '833')  ->  732  confidence: 94 % support: 0.10327
Rule  2   ('732', '833')  ->  472  confidence: 93 % support: 0.10327
Rule  3   ('833', '885')  ->  732  confidence: 93 % support: 0.10123
Rule  4   ('732', '885')  ->  472  confidence: 92 % support: 0.10838
Rule  5   ('472', '737')  ->  732  confidence: 92 % support: 0.10634
Rule  6   ('732', '833')  ->  885  confidence: 91 % support: 0.10123
Rule  7   ('472', '732')  ->  885  confidence: 91 % support: 0.10838
```

## Implementation with Kaggle Dataset
### result of Apriori Algorithm
#### result from WEKA

|||
|---|---|
|![](https://i.imgur.com/vRLcY1C.png =400x)|![](https://i.imgur.com/9g5SyC1.png =400x)|


support = 0.05(56.95/1139)
confidence = 0.9

#### result from implementation
```
Rule  1   ['laundry detergent', 'juice']  ->  vegetables  confidence: 95 % support: 0.06234
Rule  2   ['laundry detergent', 'ice cream']  ->  vegetables  confidence: 95 % support: 0.06058
Rule  3   ['dinner rolls', 'lunch meat']  ->  vegetables  confidence: 95 % support: 0.06058
Rule  4   ['dinner rolls', 'bagels']  ->  vegetables  confidence: 95 % support: 0.05795
Rule  5   ['dishwashing liquid/detergent', 'poultry']  ->  vegetables  confidence: 95 % support: 0.0755
Rule  6   ['soap', 'hand soap']  ->  vegetables  confidence: 95 % support: 0.05443
Rule  7   ['dinner rolls', 'eggs']  ->  vegetables  confidence: 95 % support: 0.0676
```

### result of FP-Growth
#### result from WEKA
|||
|---|---|
|![](https://i.imgur.com/o7vmL4Y.png =400x)|![](https://i.imgur.com/UwS4yt3.png =400x)|

support = 300
confidence = 0.9

#### result from implementation
```
Rule  1  ( 'sandwich bags', 'cheeses' ) ->  vegetables  confidence: 92 % support: 0.56102
Rule  2  ( 'soda', 'paper towels' ) ->  vegetables  confidence: 92 % support: 0.54609
Rule  3  ( 'soda', 'eggs' ) ->  vegetables  confidence: 92 % support: 0.64969
Rule  4  ( 'soda', 'shampoo' ) ->  vegetables  confidence: 92 % support: 0.54083
Rule  5  ( 'poultry', 'eggs' ) ->  vegetables  confidence: 91 % support: 0.55926
Rule  6  ( 'yogurt', 'cheeses' ) ->  vegetables  confidence: 90 % support: 0.54434
Rule  7  ( 'soap', 'pasta' ) ->  vegetables  confidence: 90 % support: 0.5259
```

## Result Comparison
### Time 
#### Comparison of difference confidence
##### IBM data
when support = 0.1(98 instances)
|Algorithm|Confidence = 0.09|Confidence = 0.9|
|---|---|---|---|---|
|Apriori|0.019737 s|0.011015 s|
|FP-Growth|0.014185 s|0.014091 s|

##### Kaggle data
when support = 0.05(300 instances)
|Algorithm|Confidence = 0.09|Confidence = 0.9|
|---|---|---|
|Apriori|216.218820 s|197.384784 s|
|FP-Growth|1.270375 s|1.056536 s|

---

#### Comparison of difference support
##### IBM data
where confidence = 0.9

Support = 0.1(98 instances)
Support = 0.05(49 instances)
Support = 0.01(25 instances)
Support = 0.005(12 instances)

|Algorithm|Support = 0.1|Support = 0.05|Support = 0.01|Support = 0.005|
|---|---|---|---|---|
|Apriori|0.019737 s|0.333576 s|2.548342 s|21.67001 s|
|FP-Growth|0.014185 s|0.173048 s|0.551261 s|6.223202 s|

##### Kaggle data
where confidence = 0.6
Support = 0.6(300 instances)
Support = 0.7(350 instances)
Support = 0.8(450 instances)
Support = 0.9(500 instances)
|Algorithm|Support = 0.6|Support = 0.7|Support = 0.8|Support = 0.9|
|---|---|---|---|---|
|Apriori|201.229253 s|148.022001 s| 162.887056s|180.557306 s|
|FP-Growth|1.0718257 s|0.956624 s| 1.060729 s|1.393035 s|

---

### Memory Usage
#### Comparison of difference confidence
##### IBM data
when support = 0.1(98 instances)
|Algorithm|Confidence = 0.09|Confidence = 0.9|
|---|---|---|
|Apriori|59588608 bytes|59576800 bytes|
|FP-Growth|60551168 bytes|60067840 bytes|

##### Kaggle data
when support = 0.05(300 instances)
|Algorithm|Confidence = 0.09|Confidence = 0.9|
|---|---|---|
|Apriori|74985472 bytes|63873024 bytes|
|FP-Growth|83083264 bytes|72679424 bytes|

---

#### Comparison of difference support
##### IBM data
where confidence = 0.9
Support = 0.1(98 instances)
Support = 0.05(49 instances)
Support = 0.01(25 instances)
Support = 0.005(12 instances)
|Algorithm|Support = 0.1|Support = 0.05|Support = 0.01|Support = 0.005|
|---|---|---|---|---|
|Apriori|59588608 bytes|59863040 bytes|62423040 bytes|81350656 bytes|
|FP-Growth|60551168 bytes|61984768 bytes|64638976 bytes|85897216 bytes|

##### Kaggle data
where confidence = 0.6
Support = 0.6(300 instances)
Support = 0.7(350 instances)
Support = 0.8(450 instances)
Support = 0.9(500 instances)
|Algorithm|Support = 0.9|Support = 0.8|Support = 0.7|Support = 0.6|
|---|---|---|---|---|
|Apriori|63504384 bytes|63862984 bytes|64307200 bytes|65635043  bytes|
|FP-Growth|73764864 bytes|73814119 bytes|73887744 bytes|74417280 bytes|

## Discussion

For the result comparison above:

### Time
#### Affect of different confidence
The time used by Apriori algorithm normally longer than that the time of FP-Growth algorithm used.

The smaller the confidence applied, the longer time taken by these algorithm

> Smaller confidence causes more transactions are chosen
> Therefore, it takes time to handle 
> 
> More transactions causes the larger the fp-tree and get longer time to search

---

#### Affect of different support
The time used by Apriori algorithm is longer than that the time of FP-Growth algorithm used, especially for the Kaggle dataset

The smaller the support given, the longer time taken by these algorithm, especially for the FP-Growth algorithm

the growing of time increasing by FP-Growth is faster than that of Apriori algorithm

> Smaller support causes more transactions are chosen
> Therefore, it takes time to handle 
> 
> More transactions causes the larger the fp-tree and get longer time to search

---

### Memory Usage
#### Affect of different confidence
The memory usage by Apriori algorithm normally larger than that the memory usage of FP-Growth algorithm.

The smaller the confidence applied, the larger memory used by these algorithm

> Smaller confidence causes more transactions are chosen
> Therefore, extra memory are needed
> 
> More transactions causes the larger the fp-tree and more memory are needed

---

#### Affect of different support
The memory used by FP-Growth algorithm normally larger than that the memory used by Apriori algorithm.

The smaller the support given, the much more memory used by these algorithm, especially for the FP-Growth algoritm, the growing of memory usage of the FP-Growth is faster than Apriori algorithm

> Smaller confidence causes more transactions are chosen
> Therefore, memory storage needed is increased
> 
> More transactions causes the larger the fp-tree and more memory are needed

---

### Dataset
The size of Kaggle dataset are much more larger than the size of IBM dataset

The time used and memory usage of Kaggle dataset are always larger than that of IBM dataset

Since all the transactions have to be scanned at least one time, **time used and memory usage are directly proportional to the number of transactions**

Because of the discrepancy of the two datasets, so different support are applied for different dataset

the proportional relationship between the support, time used and memory usage are considered

## Conclusion and Observation
In the project, Apriori algorithm and FP-Growth algorithm are excuted respectively

The effitiveness of FP-Growth algorithm is always better than that of Apriori algorithm not only of adjusting the parameters of both the algorithm but also different size of dataset

In the implementation and the expriment shown above, 
The execution of FP-Growth algorithm is always faster than the execution of Apriori algorithm, since the number of scanning the dadatabase 
 
However, the memory usage of FP-Growth algorithm is always larger than the memory usage of Apriori algorithm, since the FP-Growth algorithm needs extra memory to store and maintian the fp-tree. 

**The memory usage and the time used are inversely proportional to the value support given, when there is a fixed confidence**

**The memory usage and the time used are inversely proportional to the value confidence given, when there is a fixed support value**



