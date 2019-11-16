def even_keys(**kwargs):
    # even_args = []
    # keys = kwargs.keys()
    # for key in keys:
    #     if not len(key) % 2:
    #         even_args.append((key, kwargs[key]))
    # print(even_args)
    # return even_args

    for key, value in kwargs.items():
        if not len(key) % 2:
            print(key, value)
    # return key, value


even_keys(khag=4, fog=3, five=4, pur=3, khag02=6)
