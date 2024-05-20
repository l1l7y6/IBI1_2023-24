def chocolate_bar_calculator(total_money, price_per_bar):
    bars_afforded=total_money//price_per_bar
    #Number of chocolate bars that can be bought
    change_left=total_money%price_per_bar
    #Calculate remaining change after purchase
    return bars_afforded, change_left

total_money=int(input("All money you have"))
price=int(input("Price of one bar"))

number_of_bars, remaining_change = chocolate_bar_calculator(total_money,price)
print(f"Chocolate bars you can buy: {number_of_bars}, Change left: {remaining_change}")
#Example usage:if you import you have 100 money in all and price per bar is 7
#You will get :Chocolate bars you can buy: 14, Change left: 2