#!/usr/bin/env python

layers1 = int(raw_input('\033[1;33mEnter layers of 1st choice: '))
leafs1 = int(raw_input('\033[1;33mEnter leafs of 1st choice: '))
price1 = float(raw_input('\033[1;33mEnter price of 1st choice: '))
layer_sum1 = layers1 * leafs1 
layer_price1 = price1 / layer_sum1 

layers2 = int(raw_input('\033[1;35mEnter layers of 2nd choice: '))
leafs2 = int(raw_input('\033[1;35mEnter leafs of 2nd choice: '))
price2 = float(raw_input('\033[1;35mEnter price of 2nd choice: '))
layer_sum2 = layers2 * leafs2 
layer_price2 = price2 / layer_sum2 

if price1 < price2:
  print "\033[1;30mChoice 1 is better"
elif price1 > price2:
  print "\033[1;30mChoice 2 is better"
else:
  print "\033[1;30mPrice is the same"
