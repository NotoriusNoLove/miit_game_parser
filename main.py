from db import *


def main():
    create_table()
    games_list = [386360, 570, 444090,
                  252490, 271590, 227300,
                  730, 440, 578080]
    for item in games_list:
        insert(number=item)
    print(get_all())

# if __name__ == '__main__':
#     main()
