p_tot = []
for x in range(2, 101):
    for y in range(2, 101):
        if y > x and x + y <= 100 and x*y not in p_tot:
            p_tot.append(x*y)

p_tot = sorted(p_tot)


def divs_pair(p):
    divs = []
    pair = []
    for i in range(2, p):
        if p % i == 0 and i not in divs:
            divs.append(p//i)
            pair.append((i, p//i))
    return pair


p_pos = []
for p in p_tot:
    cdt_pair = []
    for pair in divs_pair(p):
        if pair[0] < pair[1] and pair[0] + pair[1] <= 100:
            cdt_pair.append(pair)
    if len(cdt_pair) >= 2:
        p_pos.append(p)

s_tot = [s for s in range(5, 101)]
s_pos = []
for s in s_tot:
    o = 0
    n = 0
    for i in range(2, s//2+1):
        o += 1
        a = i
        b = s-i
        if a*b in p_pos:
            n += 1
    if n == o:
        s_pos.append(s)

s_pos_p_aso = []
for s in s_pos:
    s_pos_p_aso.append(s)
    for i in range(2, s//2+1):
        a = i
        b = s-i
        if a*b in p_pos:
            s_pos_p_aso.append(a*b)

s_pos_p_aso_wdouble = []
double = []
for i in s_pos_p_aso:
    if i not in s_pos_p_aso_wdouble:
        s_pos_p_aso_wdouble.append(i)
    elif not i in double:
        double.append(i)

for i in s_pos_p_aso_wdouble:
    if i not in double and not i in s_pos:
        print(i)
    elif i in s_pos:
        input()
        print(i, ':')

















