from mygrader import Tester


def patterned_message(message, pattern):
    message = message.replace(' ', '')
    if pattern == '':
        return

    if pattern[0] == '*':
        print(message[0], end='')
        patterned_message(message[1:] + message[0], pattern[1:])
    else:
        print(pattern[0], end='')
        patterned_message(message, pattern[1:])


if __name__ == '__main__':
    tester = Tester(2023, runtime_limit=10, show_table=True, debug=True, more_detail=True)
    tester.run_test(patterned_message, num_test_cases=1)
