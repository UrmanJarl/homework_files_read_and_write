with open('1.txt', 'r', encoding='utf-8') as a:
    f1 = len(a.readlines())
with open('2.txt', 'r', encoding='utf-8') as b:
    f2 = len(b.readlines())
with open('3.txt', 'r', encoding='utf-8') as c:
    f3 = len(c.readlines())

def a_rewrite():
    with open('join_text.txt', 'a', encoding='utf-8') as f:
        f.write('1.txt\n')
        f.write(str(f1))
        f.write('\n')
        with open('1.txt', 'r', encoding='utf-8') as a:
            f.write(a.read())
            f.write('\n\n')

def b_rewrite():
    with open('join_text.txt', 'a', encoding='utf-8') as f:
        f.write('2.txt\n')
        f.write(str(f2))
        f.write('\n')
        with open('2.txt', 'r', encoding='utf-8') as b:
            f.write(b.read())
            f.write('\n\n')

def c_rewrite():
    with open('join_text.txt', 'a', encoding='utf-8') as f:
        f.write('3.txt\n')
        f.write(str(f3))
        f.write('\n')
        with open('3.txt', 'r', encoding='utf-8') as c:
            f.write(c.read())
            f.write('\n\n')


if f1 > f2 and f1 > f3:
    a_rewrite()
    if f2 > f3:
        b_rewrite()
        c_rewrite()
    else:
        c_rewrite()
        b_rewrite()
elif f2 > f1 and f2 > f3:
    b_rewrite()
    if f1 > f3:
        a_rewrite()
        c_rewrite()
    else:
        c_rewrite()
        a_rewrite()
else:
    c_rewrite()
    if f1 > f2:
        a_rewrite()
        b_rewrite()
    else:
        b_rewrite()
        a_rewrite()
