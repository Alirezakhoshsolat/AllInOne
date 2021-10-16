def sms_cost(smstext, cost, count=0):
    tedad_horoof = len(smstext)
    if tedad_horoof < 24:
        cost = 100
        print(cost)
    else:
        count = tedad_horoof // 24
        cost = (count * 247) + cost
        htoman = cost // 10
        print('cost of your SMS text is ', cost, ' Rial equal to', htoman, ' Toman.')
