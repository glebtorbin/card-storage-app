import random

def generator():
    number: str = ''
    for i in range(13):
        i = random.randint(0, 9)
        number+=str(i)
    return int(number)
