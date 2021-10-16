def pass_exam ( d, t):
    #maghadir komaki va sort cardane do list dade shode
    
    PassEx=[]
    FailEx=[]
    StartStudy = 0
    D_T = zip(d , t)
    D_T = sorted(D_T , key = lambda x: x[0])
    date , time = zip (*D_T)
    
    # ijad do list ghabooli va radi doroos

    for i in range(len(date)):
        if date[i] >= time [i]:
            PassEx.append((date[i] , time[i]))
        elif date[i] < time[i] :
            FailEx.append((date[i] , time[i]))
    
    for j in range (len(PassEx)):
        EndStudy = StartStudy + PassEx[j][1]
        if EndStudy > PassEx[j][0]:
            break
        #print ("for the exam in day" , PassEx[j][0], "you must start to study from day" , StartStudy, "till day " , EndStudy )
        else:
            print ("for the exam in day" , PassEx[j][0], "you must start to study from day" , StartStudy, "till day " , EndStudy )
            StartStudy = EndStudy



