#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        k = add(a, b)
        for m in range(4, 6):
            k = add(k, m)
        return (k)

    else:
        return(sub(a, b))
