class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text


def make_only_digit_lst(user_d=0):
    """With helps of this func we`ll check is 'user_d' digit or not, if positive it`ll be added to 'user_d_lst',
    if not, we`ll handle it with NotNumberError exception"""

    user_d_lst = []
    while user_d != 'stop':
        try:
            user_d = input('Please enter digit to add at the list: ')
            if not user_d.isdigit():
                raise NotNumberError(f'-<|>- ERROR: NotNumberError: "{user_d}" is not a digit -<|>-')
            user_d_lst.append(user_d)
            print(f'"{user_d}" is a digit, added to the user_d_lst')
        except NotNumberError as err:
            print(err)

    print(f'<---- List with digits: {user_d_lst} ---->')

if __name__ == '__main__':
    make_only_digit_lst()
