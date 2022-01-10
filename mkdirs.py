import os

dates = {
    'devops': ['01-10', '01-12', '01-19', '01-20', '01-25', '02-02', '02-03'],
    'python': ['01-10', '01-19', '01-26', '02-03', '02-07']
    + ['02-21', '02-28', '03-03', '03-07', '03-10', '03-14'],
    'ai': ['03-02', '03-03', '03-09', '03-16', '03-17', '03-21', '03-23'],
}

for k,v in dates.items():
    print(k, v, sep='\t')

for course in dates.keys():
    for date in dates[course]:
        dirname = os.path.join(course, date)
        os.makedirs(dirname, exist_ok=True)
        f = open(os.path.join(dirname, 'README.MD'), 'w')
        f.write("")
        f.close()
        
        
        

