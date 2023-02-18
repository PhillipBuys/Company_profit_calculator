for c in range(10):

    data = input()

    profit1, profit2, profit3, profit4, profit5 = data.split(",")

    profit = int(profit1)+int(profit2)+int(profit3)+int(profit4)+int(profit5)

    print(f"Company {c+1} profit: {profit}")
