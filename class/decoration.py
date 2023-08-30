# class person:
#     def do_somthing(self):
#         print('hello')
#     @classmethod
#     def age(cls):
#         cls.do_somthing()
# Person.do_somthing()
def hello(test):
        if test()>9:
           print('hello world')    
           return test
        else:
            print('you are not welcome')
            return test
@hello
def say_somth():
    return 10
