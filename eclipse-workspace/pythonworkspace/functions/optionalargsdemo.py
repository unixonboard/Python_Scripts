'''def myfun(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)
myfun(10, 20, name="Thakur", sal=10000000)'''


'''
def myfun(x, *args, **kwargs):
    print(x)
    for each in args:
        print(each)
    for k, v in kwargs.items():
        print(k,v)
myfun(10, 20, 30, 40, name="Thakur", sal=10000000)'''

#POS - positional  parameter

'''def myfun(x, *pos_param, **key_param):
    print(x)
    for each_arg in pos_param:
        print(each_arg)
    for k, v in key_param.items():
        print(k,v)
    my_fun2(*pos_param, **key_param)
    
def my_fun2(*args,**kwargs):
    print(args)
    print(kwargs)'''
    
 

# '''

def myfun(x, *pos_param, **key_param):
    print(x)
    key_param['id'] = 123;
    for each_arg in pos_param:
        print(each_arg)
    for k, v in key_param.items():
        print(k,v)
    modified_pos_param = pos_param+(50,)
    my_fun2(*modified_pos_param, **key_param)

def my_fun2(*args,**kwargs):
    print(args)
    print(kwargs)
# '''
    
myfun(10, 20, 30, 40, name="Thakur", sal=10000000)  
