def output_data(argv):
    # program, *args = argv
    with open('bakery_data.csv', 'r', encoding='utf-8') as f:
        _buh_data = f.readlines()
        buh_data = [*map(lambda k: k[:-1], _buh_data)]
        if len(argv) == 1:
            for i in buh_data:
                print(i)
        elif len(argv) == 2:
            for i in buh_data[int(argv[1]):]:
                print(i)
        elif len(argv) == 3:
            for i in buh_data[int(argv[1]) - 1:int(argv[2])]:
                print(i)
        else:
            sys.exit(1)


if __name__ == '__main__':
   import sys

   exit(output_data(sys.argv))
