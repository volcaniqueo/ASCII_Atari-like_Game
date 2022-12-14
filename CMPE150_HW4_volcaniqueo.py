
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
m_d = {}
ast_control = 'ne jouer pas'
for a in range(1, g + x + 2):
    for b in range(1, y + 1):
        z = str(a).rjust(2, '0') + str(b).rjust(2, '0')
        if a <= x:
            m_d[z] = '*'
            ast_control = 'jouer'
        elif a <= g + x + 1:
            if y % 2 == 1 and a == g + x + 1 and b == y // 2 + 1:
                position = str(a).rjust(2, '0') + str(b).rjust(2, '0')
                m_d[position] = '@'
            elif y % 2 == 0 and a == g + x + 1 and b == y // 2:
                position = str(a).rjust(2, '0') + str(b).rjust(2, '0')
                m_d[position] = '@'
            else:
                m_d[z] = ' '
if ast_control == 'ne jouer pas':
    pass
else:
    for c in m_d:
        print(m_d[c], end='')
        if int(c[2:]) == y:
            print()
control = 'oui'
if ast_control == 'ne jouer pas':
    print('YOU WON')
    for vlk in range(x + g):
        print(' ')
    print('@')
print('-' * 72)
if ast_control == 'ne jouer pas':
    print('YOUR SCORE: 0')
    control = 'non'
time = 0
while control == 'oui':
    mid_control = 'oui'
    inp = input('Choose your action! ')
    inps = inp.strip()
    inpsl = inp.lower()
    if inpsl == 'right':
        if int(position[2:]) == y:
            pass
        else:
            m_d[position] = ' '
            position = str(int(position) + 1).rjust(4, '0')
            m_d[position] = '@'
    if inpsl == 'left':
        if int(position[2:]) == 1:
            pass
        else:
            m_d[position] = ' '
            position = str(int(position) - 1).rjust(4, '0')
            m_d[position] = '@'
    if inpsl == 'fire':
        firepos = str(int(position) - 100).rjust(4, '0')
        while m_d[firepos] == ' ':
            m_d[firepos] = '|'
            for c in m_d:
                print(m_d[c], end='')
                if int(c[2:]) == y:
                    print()
            print('-' * 72)
            m_d[firepos] = ' '
            if firepos[0:2] == '01':
                break
            firepos = str(int(firepos) - 100).rjust(4, '0')
        m_d[firepos] = ' '
        wincontrol = 'voila'
        for won in m_d:
            if m_d[won] == '*':
                wincontrol = 'ne pas'
        if wincontrol == 'voila':
            print('YOU WON!')
            for c in m_d:
                print(m_d[c], end='')
                if int(c[2:]) == y:
                    print()
            print('-' * 72)
            ast_count = 0
            for vol in m_d:
                if m_d[vol] == '*':
                    ast_count = ast_count + 1
            score_count = (x * y) - ast_count
            print('YOUR SCORE:', score_count)
            control = 'non'
    if control == 'non':
        break
    if inpsl == 'exit':
        ast_count = 0
        for vol in m_d:
            if m_d[vol] == '*':
                ast_count = ast_count + 1
        score_count = (x * y) - ast_count
        for c in m_d:
            print(m_d[c], end='')
            if int(c[2:]) == y:
                print()
        print('-' * 72)
        print('YOUR SCORE:', score_count)
        control = 'non'
        mid_control = 'non'
        time = 0
    time = time + 1
    if time % 5 == 0:
        row = time // 5
        game_control = 'oui'
        for i in m_d:
            if int(i[0:2]) == x + g:
                if m_d[i] == '*':
                    game_control = 'non'
                    break
        if game_control == 'non':
            print('GAME OVER')
            for c in m_d:
                print(m_d[c], end='')
                if int(c[2:]) == y:
                    print()
            print('-' * 72)
            ast_count = 0
            for vol in m_d:
                if m_d[vol] == '*':
                    ast_count = ast_count + 1
            score_count = (x * y) - ast_count
            print('YOUR SCORE:', score_count)
            mid_control = 'non'
            control = 'non'
        else:
            list_1 = list()
            near_ast_len_val = 0
            for a in m_d:
                if m_d[a] == '*' and int(a[0:2]) > near_ast_len_val:
                    near_ast_len_val = int(a[0:2])
            for c in m_d:
                if int(c[0:2]) <= near_ast_len_val:
                    list_1.append(c)
            list_1.reverse()
            for c in list_1:
                m_d[str(int(c) + 100).rjust(4, '0')] = m_d[c]
            for c in m_d:
                if int(c[0:2]) == row:
                    m_d[c] = ' '
            for c in m_d:
                print(m_d[c], end='')
                if int(c[2:]) == y:
                    print()
            print('-' * 72)
            mid_control = 'non'
    if mid_control == 'non':
        continue
    for c in m_d:
        print(m_d[c], end='')
        if int(c[2:]) == y:
            print()
    print('-' * 72)




# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
