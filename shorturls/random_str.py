import random

def rand_str():
        a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        i = 0
        text = ''
        while i < 5:
                i += 1
                text += a[int(random.random() * len(a))]
        return text