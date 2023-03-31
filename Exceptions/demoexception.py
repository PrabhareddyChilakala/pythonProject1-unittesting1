def demo():
    # a=10
    # b=20
    # c=2
    # print(a+b/c)
    # print((a+b)/c)
    # a=10
    # b='hcl'
    # print(a*b) #prints hcl for 10 times
    # print(a+b) #occurs type error since a is integer and b is string

    # a=int("hcl")
    # print(a)#ValueError: invalid literal for int() with base 10: 'hcl'

    #try and except examples:
    # a=10
    # # b=5
    # b=0
    # try:
    #     print(a/b)
    # except Exception as e:
    #     print("error is:",e) #if b is 0 then except will executes
        # error is: division by zero

    try:
        x=int(input("enter the 1st num:"))
        y=int(input("enter the 2nd num:"))
        print(x/y)
    except ValueError as e:
        print("error is:",e)
    except ZeroDivisionError as k:
        print("error is:",k)
    else:
        print("from else")
    finally:
        print("from finally")
demo()

# outputs:
# for ZeroDivisionError:
# enter the 1st num:12
# enter the 2nd num:0
# error is: division by zero
# from finally
#
# for value error
# enter the 1st num:12
# enter the 2nd num:k
# error is: invalid literal for int() with base 10: 'k'
# from finally

