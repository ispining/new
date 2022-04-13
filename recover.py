from random import choice as cho

def gen_recovery_key(upper = False):
    lst = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if upper:
        lst = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    paragraph1 = cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst)
    paragraph2 = cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst)
    paragraph3 = cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst)
    paragraph4 = cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst)
    paragraph5 = cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst)
    paragraph6 = cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst) + cho(lst)

    return str(f"{paragraph1}-{paragraph2}-{paragraph3}-{paragraph4}-{paragraph5}-{paragraph6}")

print(gen_recovery_key().lower())
print(gen_recovery_key(upper=True))
