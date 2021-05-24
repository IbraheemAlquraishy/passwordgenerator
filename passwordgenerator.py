import random
import string



lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation


def generate(length):
    letters=lower+upper+num+symbols
    passw=random.sample(letters,length)
    return "".join(passw)


print("This is a simple password generator programmed by Ibraheem Al_quraishy")
leng=int(input("Enter password length:"))
password=generate(leng)
print(password)

