cat companiesthismonth.txt | grep $(grep -oP '([0-9]+\.[0-9]*)' companiesthismonth.txt | while read num1; read num2; do echo "$num1 $num2"; done | awk -F" " '{print $1/$2, $1}' | sort -r | while read line; do echo ${line##* }; done | head -n1)
#Cox & Kings Ltd. ! total_net_current_assets: 4389.48 ! current_liabilities_and_provisions: 509.51
