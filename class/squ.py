# def squareofnum (num):
#     assert  'error message input the invalid num'
#     return(num^2)
# num=int(input("enter your num:"))
# squareofnum(num^2)
while True:
    try:
        num=int(input("enter your num:"))
        if num < 0:
            raise ValueError('invalid number')
        ans = num**2
        print('the square of user ', 'is', ans)
    except ValueError:
        print("inproper num")
    
