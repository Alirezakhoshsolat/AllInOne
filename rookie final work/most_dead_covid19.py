
def dead_count (Date, NewDead):

    dead = zip(NewDead , Date)
    mostdead = max(sorted(dead, key=lambda x:x[0]))
    print('the most death case happened in this date : ' , mostdead[1])


