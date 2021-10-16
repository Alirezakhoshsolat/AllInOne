
def infected_count(Date, NewCase):

    case = zip(NewCase, Date)
    mostcase = max(sorted(case, key= lambda x:x[0]))
    print('the most new case happened in this date : ' ,mostcase[1])
