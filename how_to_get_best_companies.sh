cat companiesthismonth.txt | grep $(grep -oP '([0-9]+\.[0-9]*)' companiesthismonth.txt | while read num1; read num2; do echo "$num1 $num2"; done | awk -F" " '{print $1/$2, $1}' | sort -r | while read line; do echo ${line##* }; done | head -n1)
#Cox & Kings Ltd. ! total_net_current_assets: 4389.48 ! current_liabilities_and_provisions: 509.51

## how to find the top 10 companies

```
saionee@saioneePC:~/opensource/stock-analysis$ grep -Eo '[0-9]+' companiesthismonth.txt | sort -rn | head -n 5
183195
99604
94890
87397
59800
saionee@saioneePC:~/opensource/stock-analysis$ cat companiesthismonth.txt | grep 183195
LIC Housing Finance Ltd. ! total_net_current_assets: 183195.37 ! current_liabilities_and_provisions: 13657.19
saionee@saioneePC:~/opensource/stock-analysis$ cat companiesthismonth.txt | grep 99604
Shriram Transport Finance Company Ltd. ! total_net_current_assets: 99604.13 ! current_liabilities_and_provisions: 1541.8
saionee@saioneePC:~/opensource/stock-analysis$ cat companiesthismonth.txt | grep 94890
Bajaj Finance Ltd. ! total_net_current_assets: 94890.61 ! current_liabilities_and_provisions: 2584.52
saionee@saioneePC:~/opensource/stock-analysis$ cat companiesthismonth.txt | grep 87397
Indiabulls Housing Finance Ltd. ! total_net_current_assets: 87397.03 ! current_liabilities_and_provisions: 6639.21
saionee@saioneePC:~/opensource/stock-analysis$ cat companiesthismonth.txt | grep 59800
Mahindra & Mahindra Financial Services Ltd. ! total_net_current_assets: 59800.19 ! current_liabilities_and_provisions: 3323.03
saionee@saioneePC:~/opensource/stock-analysis$ grep -Eo '[0-9]+' companiesthismonth.txt | sort -rn | head -n 10
183195
99604
94890
87397
59800
56493
56493
35427
28015
27878
```
