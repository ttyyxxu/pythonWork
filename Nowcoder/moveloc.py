import re

inputstr = "A10;S20;W10;D30;X;A1A;B10A11;;A10;"

print(re.split(r'[\s\;]',inputstr))

# action_list = [re.match(r'^\s*([ASDW][0-9]+)\s*$',i) for i in inputstr.split(';')]
#
# valid_actions = [i.groups()[0] for i in action_list if i is not None]
#
#
# loc = (0,0)
#
# for action in valid_actions:
#     if action.startswith('A'):
#         loc = loc[0] - int(action[1:]), loc[1]
#     elif action.startswith('W'):
#         loc = loc[0], loc[1] + int(action[1:])
#     elif action.startswith('S'):
#         loc = loc[0], loc[1] - int(action[1:])
#     elif action.startswith('D'):
#         loc = loc[0] + int(action[1:]), loc[1]
#
#
# print(loc[0], loc[1], sep=',')