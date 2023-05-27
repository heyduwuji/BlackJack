card = [1,2,3,4,5,6,7,8,9,10,10,10,10]

dealer_bust = 0.0
dealer_value = {}

def simulate(point, prob):
    global dealer_bust
    global dealer_value
    for x in card:
        if point+x > 21:
            dealer_bust += prob/13.0
            continue
        elif point+x >= 17:
            if str(point+x) in dealer_value:
                dealer_value[str(point+x)] += prob/13.0
            else:
                dealer_value[str(point+x)] = prob/13.0
            continue
        else:
            simulate(point+x, prob/13.0)
    return

for exposed in card:
    print("when dealer's exposed card is {}".format(exposed))
    dealer_bust = 0.0
    dealer_value = {}
    for hidden in card:
        if exposed+hidden > 21:
            continue
        elif exposed+hidden >= 17:
            if str(exposed+hidden) in dealer_value:
                dealer_value[str(exposed+hidden)] += 1.0/13.0
            else:
                dealer_value[str(exposed+hidden)] = 1.0/13.0
        else:
            simulate(exposed+hidden, 1.0/13.0)
    print("bust prob: {}".format(round(dealer_bust, 4)))
    for (key, value) in dealer_value.items():
        print("dealer's final point is: {} prob: {}".format(key, round(value, 4)))
