def show_info(name, *var_args):
    print(name)
    for item in var_args:
        print(item)
    return


show_info('A', 'B', 20, 'xyz')
