import time

line0 = 100000000000000000000000000000000000000000000000000
line1 = 100000000000000000000000000000000000000000000000000
line2 = 100000000000000000000000000000000000000000000000000
line3 = 100000000000000000000000000000000000000000000000000
line4 = 100000000000000000000000000000000000000000000000000
line5 = 100000000000000000000000000000000000000000000000000
line6 = 100000000000000000000000000000000000000000000000000
line7 = 100000000000000000000000000000000000000000000000000
line8 = 100000000000000000000000000000000000000000000000000
line9 = 100000000000000000000000000000000000000000000000000
line10 = 100000000000000000000000000000000000000000000000000
line11 = 100000000000000000000000000000000000000000000000000
line12 = 100000000000000000000000000000000000000000000000000
line13 = 100000000000000000000000000000000000000000000000000
line14 = 100000000000000000000000000000000000000000000000000
line15 = 100000000000000000000000000000000000000000000000000
line16 = 100000000000000000000000000000000000000000000000000
line17 = 100000000000000000000000000000000000000000000000000
line18 = 100000000000000000000000000000000000000000000000000
line19 = 100000000000000000000000000000000000000000000000000

p0 = -1  # 中心x
q0 = -1  # 中心y
pq0 = -1  # 発生時間

p1 = -1
q1 = -1
pq1 = -1

p2 = -1
q2 = -1
pq2 = -1

p3 = -1
q3 = -1
pq3 = -1

p4 = -1
q4 = -1
pq4 = -1

p5 = -1
q5 = -1
pq5 = -1

LOOP = 9+1  # 最大
SKIP = 1  # 飛ばす数
SLEEP_TIME = 0.01  # コマ時間

PI = 3.14159265358979323846  # 円周率

A, C, M = 1664525, 1013904223, 2**32  # 線形合同法 パラメータ
xx = 12
yy = 7

u = -1
t = 0
while t < 10000000:
    xx = (A*xx+C) % M
    yy = (A*yy+C) % M
    x = xx % 50  # x座標 0-index
    y = yy % 20  # y座標 0-index

    if t % 11 == 0:  # 11t につき一回発生
        u = u+1
        if u == 0:
            p0 = x
            q0 = y
            pq0 = t
        if u == 1:
            p1 = x
            q1 = y
            pq1 = t
        if u == 2:
            p2 = x
            q2 = y
            pq2 = t
        if u == 3:
            p3 = x
            q3 = y
            pq3 = t
        if u == 4:
            p4 = x
            q4 = y
            pq4 = t
            u = -1
        if u == 5:
            p5 = x
            q5 = y
            pq5 = t

    k = 0
    while k < 5:
        hline0 = 100000000000000000000000000000000000000000000000000
        hline1 = 100000000000000000000000000000000000000000000000000
        hline2 = 100000000000000000000000000000000000000000000000000
        hline3 = 100000000000000000000000000000000000000000000000000
        hline4 = 100000000000000000000000000000000000000000000000000
        hline5 = 100000000000000000000000000000000000000000000000000
        hline6 = 100000000000000000000000000000000000000000000000000
        hline7 = 100000000000000000000000000000000000000000000000000
        hline8 = 100000000000000000000000000000000000000000000000000
        hline9 = 100000000000000000000000000000000000000000000000000
        hline10 = 100000000000000000000000000000000000000000000000000
        hline11 = 100000000000000000000000000000000000000000000000000
        hline12 = 100000000000000000000000000000000000000000000000000
        hline13 = 100000000000000000000000000000000000000000000000000
        hline14 = 100000000000000000000000000000000000000000000000000
        hline15 = 100000000000000000000000000000000000000000000000000
        hline16 = 100000000000000000000000000000000000000000000000000
        hline17 = 100000000000000000000000000000000000000000000000000
        hline18 = 100000000000000000000000000000000000000000000000000
        hline19 = 100000000000000000000000000000000000000000000000000
        rad = 0
        tt = 0  # 時間の差 = 半径
        px = 0
        qy = 0
        if k == 0:
            tt = t - pq0
            px = p0
            qy = q0
        if k == 1:
            tt = t - pq1
            px = p1
            qy = q1
        if k == 2:
            tt = t - pq2
            px = p2
            qy = q2
        if k == 3:
            tt = t - pq3
            px = p3
            qy = q3
        if k == 4:
            tt = t - pq4
            px = p4
            qy = q4
        if k == 5:
            tt = t - pq5
            px = p5
            qy = q5

        # 計算量改善
        if px**2+qy**2 < tt and (px-49)+qy**2 < tt and px**2+(qy-19)**2 < tt and (px-49)**2+(qy-19)**2 < tt:
            px = 0

        while px >= 0 and rad < 2*PI:
            sin = rad
            cos = PI/2 - rad
            fas = rad
            fac = PI/2 - rad
            i = 1
            while i < 10:
                fas = fas * -((rad**2)/((2*i+1)*(2*i)))
                fac = fac * -(((PI/2 - rad)**2)/((2*i+1)*(2*i)))
                sin = sin + fas
                cos = cos + fac
                i = i+1

            tx = px + int(sin * tt)
            ty = qy + int(cos * tt)
            rad = rad+0.01

            if ty == 0:
                if 0 <= tx < 50 and hline0 // 10**tx % 10 == 0:
                    hline0 = hline0 + 10**tx
            if ty == 1:
                if 0 <= tx < 50 and hline1 // 10**tx % 10 == 0:
                    hline1 = hline1 + 10**tx
            if ty == 2:
                if 0 <= tx < 50 and hline2 // 10**tx % 10 == 0:
                    hline2 = hline2 + 10**tx
            if ty == 3:
                if 0 <= tx < 50 and hline3 // 10**tx % 10 == 0:
                    hline3 = hline3 + 10**tx
            if ty == 4:
                if 0 <= tx < 50 and hline4 // 10**tx % 10 == 0:
                    hline4 = hline4 + 10**tx
            if ty == 5:
                if 0 <= tx < 50 and hline5 // 10**tx % 10 == 0:
                    hline5 = hline5 + 10**tx
            if ty == 6:
                if 0 <= tx < 50 and hline6 // 10**tx % 10 == 0:
                    hline6 = hline6 + 10**tx
            if ty == 7:
                if 0 <= tx < 50 and hline7 // 10**tx % 10 == 0:
                    hline7 = hline7 + 10**tx
            if ty == 8:
                if 0 <= tx < 50 and hline8 // 10**tx % 10 == 0:
                    hline8 = hline8 + 10**tx
            if ty == 9:
                if 0 <= tx < 50 and hline9 // 10**tx % 10 == 0:
                    hline9 = hline9 + 10**tx
            if ty == 10:
                if 0 <= tx < 50 and hline10 // 10**tx % 10 == 0:
                    hline10 = hline10 + 10**tx
            if ty == 11:
                if 0 <= tx < 50 and hline11 // 10**tx % 10 == 0:
                    hline11 = hline11 + 10**tx
            if ty == 12:
                if 0 <= tx < 50 and hline12 // 10**tx % 10 == 0:
                    hline12 = hline12 + 10**tx
            if ty == 13:
                if 0 <= tx < 50 and hline13 // 10**tx % 10 == 0:
                    hline13 = hline13 + 10**tx
            if ty == 14:
                if 0 <= tx < 50 and hline14 // 10**tx % 10 == 0:
                    hline14 = hline14 + 10**tx
            if ty == 15:
                if 0 <= tx < 50 and hline15 // 10**tx % 10 == 0:
                    hline15 = hline15 + 10**tx
            if ty == 16:
                if 0 <= tx < 50 and hline16 // 10**tx % 10 == 0:
                    hline16 = hline16 + 10**tx
            if ty == 17:
                if 0 <= tx < 50 and hline17 // 10**tx % 10 == 0:
                    hline17 = hline17 + 10**tx
            if ty == 18:
                if 0 <= tx < 50 and hline18 // 10**tx % 10 == 0:
                    hline18 = hline18 + 10**tx
            if ty == 19:
                if 0 <= tx < 50 and hline19 // 10**tx % 10 == 0:
                    hline19 = hline19 + 10**tx

        rad = 0
        while px >= 0 and rad < 2*PI:
            sin = rad
            cos = PI/2 - rad
            fas = rad
            fac = PI/2 - rad
            i = 1
            while i < 10:
                fas = fas * -((rad**2)/((2*i+1)*(2*i)))
                fac = fac * -(((PI/2 - rad)**2)/((2*i+1)*(2*i)))
                sin = sin + fas
                cos = cos + fac
                i = i+1

            ttx = px + int(sin * (tt-1))  # 一つ前の時間
            tty = qy + int(cos * (tt-1))
            rad = rad+0.01

            if tt == 0:
                px = -1
            elif tty == 0:
                if 0 <= ttx < 50 and hline0 // 10**ttx % 10 == 1:
                    hline0 = hline0 - 10**ttx
            elif tty == 1:
                if 0 <= ttx < 50 and hline1 // 10**ttx % 10 == 1:
                    hline1 = hline1 - 10**ttx
            elif tty == 2:
                if 0 <= ttx < 50 and hline2 // 10**ttx % 10 == 1:
                    hline2 = hline2 - 10**ttx
            elif tty == 3:
                if 0 <= ttx < 50 and hline3 // 10**ttx % 10 == 1:
                    hline3 = hline3 - 10**ttx
            elif tty == 4:
                if 0 <= ttx < 50 and hline4 // 10**ttx % 10 == 1:
                    hline4 = hline4 - 10**ttx
            elif tty == 5:
                if 0 <= ttx < 50 and hline5 // 10**ttx % 10 == 1:
                    hline5 = hline5 - 10**ttx
            elif tty == 6:
                if 0 <= ttx < 50 and hline6 // 10**ttx % 10 == 1:
                    hline6 = hline6 - 10**ttx
            elif tty == 7:
                if 0 <= ttx < 50 and hline7 // 10**ttx % 10 == 1:
                    hline7 = hline7 - 10**ttx
            elif tty == 8:
                if 0 <= ttx < 50 and hline8 // 10**ttx % 10 == 1:
                    hline8 = hline8 - 10**ttx
            elif tty == 9:
                if 0 <= ttx < 50 and hline9 // 10**ttx % 10 == 1:
                    hline9 = hline9 - 10**ttx
            elif tty == 10:
                if 0 <= ttx < 50 and hline10 // 10**ttx % 10 == 1:
                    hline10 = hline10 - 10**ttx
            elif tty == 11:
                if 0 <= ttx < 50 and hline11 // 10**ttx % 10 == 1:
                    hline11 = hline11 - 10**ttx
            elif tty == 12:
                if 0 <= ttx < 50 and hline12 // 10**ttx % 10 == 1:
                    hline12 = hline12 - 10**ttx
            elif tty == 13:
                if 0 <= ttx < 50 and hline13 // 10**ttx % 10 == 1:
                    hline13 = hline13 - 10**ttx
            elif tty == 14:
                if 0 <= ttx < 50 and hline14 // 10**ttx % 10 == 1:
                    hline14 = hline14 - 10**ttx
            elif tty == 15:
                if 0 <= ttx < 50 and hline15 // 10**ttx % 10 == 1:
                    hline15 = hline15 - 10**ttx
            elif tty == 16:
                if 0 <= ttx < 50 and hline16 // 10**ttx % 10 == 1:
                    hline16 = hline16 - 10**ttx
            elif tty == 17:
                if 0 <= ttx < 50 and hline17 // 10**ttx % 10 == 1:
                    hline17 = hline17 - 10**ttx
            elif tty == 18:
                if 0 <= ttx < 50 and hline18 // 10**ttx % 10 == 1:
                    hline18 = hline18 - 10**ttx
            elif tty == 19:
                if 0 <= ttx < 50 and hline19 // 10**ttx % 10 == 1:
                    hline19 = hline19 - 10**ttx

        yyy = 0
        while yyy < 20:
            xxx = 0
            while xxx < 50:
                if yyy == 0 and hline0 // 10**xxx % 10 > 0:
                    if line0 // 10**xxx % 10 >= LOOP-SKIP:
                        line0 = line0 - LOOP * 10**xxx

                    line0 = line0 + SKIP * 10**xxx
                if yyy == 1 and hline1 // 10**xxx % 10 > 0:
                    if line1 // 10**xxx % 10 >= LOOP-SKIP:
                        line1 = line1 - LOOP * 10**xxx

                    line1 = line1 + SKIP * 10**xxx
                if yyy == 2 and hline2 // 10**xxx % 10 > 0:
                    if line2 // 10**xxx % 10 >= LOOP-SKIP:
                        line2 = line2 - LOOP * 10**xxx

                    line2 = line2 + SKIP * 10**xxx
                if yyy == 3 and hline3 // 10**xxx % 10 > 0:
                    if line3 // 10**xxx % 10 >= LOOP-SKIP:
                        line3 = line3 - LOOP * 10**xxx

                    line3 = line3 + SKIP * 10**xxx
                if yyy == 4 and hline4 // 10**xxx % 10 > 0:
                    if line4 // 10**xxx % 10 >= LOOP-SKIP:
                        line4 = line4 - LOOP * 10**xxx

                    line4 = line4 + SKIP * 10**xxx
                if yyy == 5 and hline5 // 10**xxx % 10 > 0:
                    if line5 // 10**xxx % 10 >= LOOP-SKIP:
                        line5 = line5 - LOOP * 10**xxx

                    line5 = line5 + SKIP * 10**xxx
                if yyy == 6 and hline6 // 10**xxx % 10 > 0:
                    if line6 // 10**xxx % 10 >= LOOP-SKIP:
                        line6 = line6 - LOOP * 10**xxx

                    line6 = line6 + SKIP * 10**xxx
                if yyy == 7 and hline7 // 10**xxx % 10 > 0:
                    if line7 // 10**xxx % 10 >= LOOP-SKIP:
                        line7 = line7 - LOOP * 10**xxx

                    line7 = line7 + SKIP * 10**xxx
                if yyy == 8 and hline8 // 10**xxx % 10 > 0:
                    if line8 // 10**xxx % 10 >= LOOP-SKIP:
                        line8 = line8 - LOOP * 10**xxx

                    line8 = line8 + SKIP * 10**xxx
                if yyy == 9 and hline9 // 10**xxx % 10 > 0:
                    if line9 // 10**xxx % 10 >= LOOP-SKIP:
                        line9 = line9 - LOOP * 10**xxx

                    line9 = line9 + SKIP * 10**xxx
                if yyy == 10 and hline10 // 10**xxx % 10 > 0:
                    if line10 // 10**xxx % 10 >= LOOP-SKIP:
                        line10 = line10 - LOOP * 10**xxx

                    line10 = line10 + SKIP * 10**xxx
                if yyy == 11 and hline11 // 10**xxx % 10 > 0:
                    if line11 // 10**xxx % 10 >= LOOP-SKIP:
                        line11 = line11 - LOOP * 10**xxx

                    line11 = line11 + SKIP * 10**xxx
                if yyy == 12 and hline12 // 10**xxx % 10 > 0:
                    if line12 // 10**xxx % 10 >= LOOP-SKIP:
                        line12 = line12 - LOOP * 10**xxx

                    line12 = line12 + SKIP * 10**xxx
                if yyy == 13 and hline13 // 10**xxx % 10 > 0:
                    if line13 // 10**xxx % 10 >= LOOP-SKIP:
                        line13 = line13 - LOOP * 10**xxx

                    line13 = line13 + SKIP * 10**xxx
                if yyy == 14 and hline14 // 10**xxx % 10 > 0:
                    if line14 // 10**xxx % 10 >= LOOP-SKIP:
                        line14 = line14 - LOOP * 10**xxx

                    line14 = line14 + SKIP * 10**xxx
                if yyy == 15 and hline15 // 10**xxx % 10 > 0:
                    if line15 // 10**xxx % 10 >= LOOP-SKIP:
                        line15 = line15 - LOOP * 10**xxx

                    line15 = line15 + SKIP * 10**xxx
                if yyy == 16 and hline16 // 10**xxx % 10 > 0:
                    if line16 // 10**xxx % 10 >= LOOP-SKIP:
                        line16 = line16 - LOOP * 10**xxx

                    line16 = line16 + SKIP * 10**xxx
                if yyy == 17 and hline17 // 10**xxx % 10 > 0:
                    if line17 // 10**xxx % 10 >= LOOP-SKIP:
                        line17 = line17 - LOOP * 10**xxx

                    line17 = line17 + SKIP * 10**xxx
                if yyy == 18 and hline18 // 10**xxx % 10 > 0:
                    if line18 // 10**xxx % 10 >= LOOP-SKIP:
                        line18 = line18 - LOOP * 10**xxx

                    line18 = line18 + SKIP * 10**xxx
                if yyy == 19 and hline19 // 10**xxx % 10 > 0:
                    if line19 // 10**xxx % 10 >= LOOP-SKIP:
                        line19 = line19 - LOOP * 10**xxx

                    line19 = line19 + SKIP * 10**xxx
                xxx = xxx+1
            yyy = yyy+1
        k = k+1

    print(line0*10+1)
    print(line1*10+1)
    print(line2*10+1)
    print(line3*10+1)
    print(line4*10+1)
    print(line5*10+1)
    print(line6*10+1)
    print(line7*10+1)
    print(line8*10+1)
    print(line9*10+1)
    print(line10*10+1)
    print(line11*10+1)
    print(line12*10+1)
    print(line13*10+1)
    print(line14*10+1)
    print(line15*10+1)
    print(line16*10+1)
    print(line17*10+1)
    print(line18*10+1)
    print(line19*10+1)
    print('')

    time.sleep(SLEEP_TIME)
    t = t+1
