import string
import random

def limits(pass_length):
    return int(pass_length * 0.5), int(pass_length * 0.25), int(pass_length * 0.25)


def password_generator(pass_length):
    letters_list = string.ascii_letters
    digits_list = string.digits
    symbols_list = string.punctuation

    letters_cnt, digits_cnt, symbols_cnt = limits(pass_length)
    if letters_cnt + digits_cnt + symbols_cnt < pass_length:
        letters_cnt += (pass_length - (letters_cnt + digits_cnt + symbols_cnt ))

    pass_list = []

    for i in range(0, letters_cnt):
        pass_list.append(letters_list[random.randint(0, len(letters_list)-1)])

    for i in range(0, digits_cnt):
        pass_list.append(digits_list[random.randint(0, len(digits_list)-1)])

    for i in range(0, symbols_cnt):
        pass_list.append(symbols_list[random.randint(0, len(symbols_list)-1)])

    random.shuffle(pass_list)
    return ''.join(pass_list)

print("You generated password is : ", password_generator(int(input("What should be the password length? "))))