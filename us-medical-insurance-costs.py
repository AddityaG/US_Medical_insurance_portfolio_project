import csv
ages = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []
with open('insurance.csv', newline='') as insurance_file:
    insurance_reader = csv.DictReader(insurance_file)
    for row in insurance_reader:
        ages.append(int(row['age']))
        sex.append(row['sex'])
        children.append(int(row['children']))
        if(row['smoker']=='yes'):
            smoker.append(1)
        else:
            smoker.append(0)
        region.append(row['region'])
        charges.append(float(row['charges']))

def average_no(listt):
    total = 0
    for i in listt:
        total+=i
    return total/len(listt)

def sex_ratio(listt):
    w = 0
    m = 0
    for i in listt:
        if(i=='male'):
            m+=1
        if(i=='female'):
            w+=1
    return str(round(m/w,2))

def cost_diff(listt):
    nsm = 0
    nsmc=0
    sm = 0
    smc=0
    for i in range(len(listt)):
        if(listt[i]==1):
            smc+=1
            sm+=charges[i]
        else:
            nsmc+=1
            nsm+=charges[i]
    avg_sm = round(sm/smc,2)
    avg_nsm = round(nsm/nsmc,2)
    return str(avg_sm)+" VS "+str(avg_nsm)

def max_freq(listt):
    freq = {}
    for i in listt:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    maxx = 0
    maxxpl=''
    for i in freq:
        if(freq[i]>maxx):
            maxx = freq[i]
            maxxpl = i
    return str(maxx)+" and the place is "+maxxpl

def average_age(listt):
    age_count = 0
    no_ppl = 0
    for i in range(len(listt)):
        if(listt[i]>=1):
            age_count+=ages[i]
            no_ppl+=1
    return str(round(age_count/no_ppl,2))

print("The average age of the dataset is "+str(round(average_no(ages),2)))
print("The ratio between male and female (m:w) candidates in the dataset is "+sex_ratio(sex))
print("The insurance cost difference between smokers and non-smokers is "+cost_diff(smoker))
print("The count of the place from where majority are from is "+max_freq(region))
print("The average age of a person with at least one child is "+average_age(children))