# This is the link to this Python coding challenge
# https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
def bool_to_word():
    boolean = input('True or False?\n').lower()
    if boolean == 'true':
        print('Yes')
    elif boolean == 'false':
        print('No')
    else:
        print('Invalid input: Choose only between True or False\n')
bool_to_word()