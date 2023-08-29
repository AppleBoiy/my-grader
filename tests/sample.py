from mygrader import Tester


def median_of_median(list_a):
    if len(list_a) == 1:
        return list_a[0]
    elif len(list_a) == 2:
        return (list_a[0] + list_a[1]) / 2

    pos3 = len(list_a) // 3

    group = [median_of_median(list_a[:pos3]),
             median_of_median(list_a[pos3:2 * pos3]),
             median_of_median(list_a[2 * pos3:])]

    middle = sum(group) - max(group) - min(group)

    return middle


if __name__ == '__main__':
    tester = Tester(2023, median_of_median, runtime_limit=3)
