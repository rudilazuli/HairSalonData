hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# step 1
total_price = 0

# step 2
for price in prices:
  total_price += price
print(total_price)

# step 3
average_price = len(prices)
print(average_price)

# step 4
print("Average Haircur Price:" + str(average_price))

# step 5 & 6
new_prices = [price - 5 for price in prices]
print(new_prices)

# step 7
total_revenue = 0

# step 8 & 9 & 10
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[1]
print('Total Revenue:' + str(total_revenue))

# step 11
average_daily_revenue = [total_revenue / 7]
print(average_daily_revenue)

# step 12 & 13
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
