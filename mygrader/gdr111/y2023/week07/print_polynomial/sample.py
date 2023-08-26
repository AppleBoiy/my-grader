def print_polynomial(pc_list, v):
    a = sorted(pc_list, key=lambda x: x[0], reverse=True)
    a = list(map(lambda x: degree(x, v), a))
    a = list(map(lambda x: check_point(x), a))
    b = list(a[:1])
    c = list(a[1:])
    c = list(map(lambda x: check_sign(x), c))
    result = b + c
    result = ''.join(result)
    return result


def degree(a, val):
    if a[0] >= 0:
        if a[0] >= 2:
            return str(a[1]) + val + '^' + str(a[0])
        elif a[0] == 1:
            return str(a[1]) + val
        else:
            return str(a[1])


def check_sign(a):
    if a[0] == '-':
        c = ' - ' + a.replace('-', '')
        return c
    else:
        c = ' + ' + a
        return c


def check_point(a):
    x = a.find('.')
    if a[x + 1] == '0' and a[x + 2] == '':
        return a.replace('.0', '')
    else:
        return a


def main():
    power = input('').split()
    power = list(map(lambda x: int(x), power))
    coe = input('').split()
    coe = list(map(lambda x: float(x), coe))
    val = input('')
    polynomial = list(zip(power, coe))
    print(print_polynomial(polynomial, val))
