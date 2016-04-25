#!/usr/bin/env python

layers1 = int(raw_input('\033[1;33mEnter layers of 1st choice: '))
leafs1 = int(raw_input('\033[1;33mEnter leafs of 1st choice: '))
price1 = float(raw_input('\033[1;33mEnter price of 1st choice: '))

layers2 = int(raw_input('\033[1;35mEnter layers of 2nd choice: '))
leafs2 = int(raw_input('\033[1;35mEnter leafs of 2nd choice: '))
price2 = float(raw_input('\033[1;35mEnter price of 2nd choice: '))

def layer_price(layers, leafs, price):
    layer_sum = layers * leafs 
    layer_price = price / layer_sum 
    return layer_price

paper_1 = layer_price(layers1, leafs1, price1)
paper_2 = layer_price(layers2, leafs2, price2)

if paper_1 < paper_2:
  print "\033[1;30mChoice 1 is better"
elif paper_1 > paper_2:
  print "\033[1;30mChoice 2 is better"
else:
  print "\033[1;30mPrice is the same"
