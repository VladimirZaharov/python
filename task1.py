with open('task1.txt', 'w') as tx:
    in_text = input()
    while bool(in_text) == True:
        tx.write(f'{in_text}\n')
        in_text = input()
