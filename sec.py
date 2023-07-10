def my_list(lst):
    return [item for item in lst if len (item) > 4]
new_list=my_list(['Queen' , 'chison' , 'precious' ,'king'])
print(new_list)