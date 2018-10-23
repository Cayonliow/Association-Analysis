# Data Mining Homework1 - Association Analysis

---

*    dataset: IBM Quest Synthetic Data Generator 
*    parameter:
        *    `ntrans`, number of transaction = 1(*1000)
        *    `tlen`, average length per transaction = 10
        *    `nitems`, number of types of item = 1(*1000)
        *    `npats`, number of pattern = 100

**minimum support = 0.1(98 instances)**
**minimum confidence = 0.9**
>accodring to the result of WEKA

```
IBM Quest Data Generator.exe" lit -ntrans 1 -tlen 10 -nitems 1 -npats 100 -fname test
```



## Apriori Algorithm
### result from WEKA
![](https://i.imgur.com/6a7jcNn.png)

### result from implementation
```
Rule  1   ('472', '885')  ->  732  confidence: 94 % support: 0.10838
Rule  2   ('472', '833')  ->  732  confidence: 94 % support: 0.10327
Rule  3   ('732', '833')  ->  472  confidence: 93 % support: 0.10327
Rule  4   ('833', '885')  ->  732  confidence: 93 % support: 0.10123
Rule  5   ('732', '885')  ->  472  confidence: 92 % support: 0.10838
Rule  6   ('472', '737')  ->  732  confidence: 92 % support: 0.10634
Rule  7   ('472', '885')  ->  737  confidence: 91 % support: 0.10532
```

## Fp-growth
### result from WEKA
![](https://i.imgur.com/RFbK53i.png)

### result from implementation
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
* dataset used: [Association of shopping basket](https://www.kaggle.com/lalalalsa/association-of-shopping-basket/data)

### result of Apriori Algorithm
![](https://i.imgur.com/vRLcY1C.png)
![](https://i.imgur.com/9g5SyC1.png)

support = 0.05(56.95/1139)
confidence = 0.9

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

![](https://i.imgur.com/o7vmL4Y.png)
![](https://i.imgur.com/UwS4yt3.png)

support = 300
confidence = 0.9

```
Rule  1  ( 'sandwich bags', 'cheeses' ) ->  vegetables  confidence: 92 % support: 0.56102
Rule  2  ( 'soda', 'paper towels' ) ->  vegetables  confidence: 92 % support: 0.54609
Rule  3  ( 'soda', 'eggs' ) ->  vegetables  confidence: 92 % support: 0.64969
Rule  4  ( 'soda', 'shampoo' ) ->  vegetables  confidence: 92 % support: 0.54083
Rule  5  ( 'poultry', 'eggs' ) ->  vegetables  confidence: 91 % support: 0.55926
Rule  6  ( 'yogurt', 'cheeses' ) ->  vegetables  confidence: 90 % support: 0.54434
Rule  7  ( 'soap', 'pasta' ) ->  vegetables  confidence: 90 % support: 0.5259
```
