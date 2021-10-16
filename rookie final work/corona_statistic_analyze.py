
import csv

import most_dead_covid19
import most_infected_covid19

def corona_statistic(a ,DATE=[], New_Case=[], Cumulative_Case=[], New_Death=[], Cumulative_Deaths=[]):
    with open(a,newline='') as Cov19 :
        covIr = csv.reader(Cov19,delimiter=';')
        line_count = 0

        for row in covIr :
            if line_count == 0 :
                print(f'Column names are {"                 ".join(row)}')
                line_count += 1
            else :
                DATE.append(row[0])
                New_Case.append(int(row[1]))
                Cumulative_Case.append(int(row[2]))
                New_Death.append(int(row[3]))
                Cumulative_Deaths.append(int(row[4]))
                print(f'\t\t         {row[0]}\t\t\t  {row[1]}\t\t\t\t\t\t\t{row[2]}\t\t\t\t\t\t\t\t {row[3]}\t\t\t\t\t\t\t{row[4]}')
                line_count += 1
        what_to_do=int(input('''what do you want to do with this data?
        
        1) show me which day had the most new death cases.
        2) show me which day had the most new infected case.'''))

        if what_to_do == 1:
            most_dead_covid19.dead_count(DATE,New_Death)
        elif what_to_do == 2:
            most_infected_covid19.infected_count(DATE,New_Case)



            

        
