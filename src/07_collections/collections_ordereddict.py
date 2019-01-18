from collections import OrderedDict

N = int(input())
cart = OrderedDict()

for _ in range(N):
    args = input().split()
    item_name = " ".join(args[:len(args) - 1])
    net_price = int(args[-1])

    if item_name in cart:
        cart[item_name] += net_price
    else:
        cart[item_name] = net_price

for k, v in cart.items():
    print(k, v)
