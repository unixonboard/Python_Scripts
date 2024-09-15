students={'john':['Python','DJango','DRF'] , 'bob':['Java','Spring'], 'jim': ['js','node','react']}
keys=students.keys()
for eachKey in keys:
    print('Cource Taken by',eachKey,'are')
    for eachCource in students[eachKey]:
        print(eachCource)
    