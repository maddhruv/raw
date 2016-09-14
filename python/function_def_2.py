def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'Y', 'YES', 'ye', 'yes'):
            return True
        if ok in ('n', 'N', 'NO', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('OK to overwrite the file?', 2)
