items = ('Apple','Pizza','spaghetti','noodle','egg')
prices = (1,5,2,.5,6)


for i in range(len(items)):
    print(f'I bought {items[i]} for {prices[i]}')

#When list1 is at i, so is list2


#Find cheapest item and most expensive


Cheapest = prices.index(min(prices))
Expensive = prices.index(max(prices))
print(f'The cheapest item was {items[Cheapest]}')
print(f'the most expensive item was {items[Expensive]}')


