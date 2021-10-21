def input_data(argv):
    program, *args = argv
    buh_list = [*args]
    buh_list_new = [*map(lambda x: f'{x}\n', buh_list)]
    # print(buh_list_new)
    with open('bakery_data.csv', 'a', encoding='utf-8') as f:
        f.writelines(buh_list_new)


if __name__ == '__main__':
   import sys

   exit(input_data(sys.argv))
