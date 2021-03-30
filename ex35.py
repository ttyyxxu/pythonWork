from sys import exit
'''
def gold_room():
    print("room full of gold")
    choice = input('>')
'''
'''
choice = input('>')

if '0' in choice or '1' in choice:
    print(choice)
else:
    print('hoops')
    print(f'and this is {choice}')
'''
i=0

while True:
    i+=1
    if(i%2==1):
        continue

    print(f"currently i = {i}")
    if i > 6:
        break
