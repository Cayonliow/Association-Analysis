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