"""这是注释这是注释
我知道你知道这是注释
但是我还是要说一遍这是注释
就是这样"""

china = ['beijing', 'tianjin', ['chuzhou', 'hefei'], 'shanghai', 'guangdong']


def print_nested_list(list_var, depth):
    for item_var in list_var:
        if isinstance(item_var, list):
            print_nested_list(item_var, depth + 1)
        else:
            for count in range(depth):
                print("\t", end='')
            print(item_var)

print_nested_list(china, -8)

print(id(china))