import numpy as np


def west(p, m, a, ms, mh, u, stepcost, gamma):
    if(ms == 0):
        p1 = 0.8
        p2 = 0.2
    else:
        p1 = 0.5
        p2 = 0.5
    ms1 = (ms+1) % 2

    t1 = stepcost + \
        (gamma * ((p2 * u[1][m][a][ms1][mh]) + (p1 * u[1][m][a][ms][mh])))
    ans = t1
    action = "RIGHT"

    t2 = stepcost + \
        (gamma * ((p2 * u[0][m][a][ms1][mh]) + (p1 * u[0][m][a][ms][mh])))
    if(ans < t2):
        ans = t2
        action = "STAY"

    if(a > 0):

        t30 = 0.25 * ((p1 * u[0][m][a-1][ms][mh-1]) +
                      (p2 * u[0][m][a-1][ms1][mh-1]))
        t31 = 0.75 * ((p1 * u[0][m][a-1][ms][mh]) +
                      (p2 * u[0][m][a-1][ms1][mh]))
        t3 = stepcost + (gamma * (t30 + t31))
        if(ms <= 1):
            t3 += 12.5
        if(ans < t3):
            ans = t3
            action = "SHOOT"
    ans1 = round(ans, 3)
    print("(" + pos[p] + "," + str(mat[m]) + "," + str(arrow[a]) + "," + str(
        mm_state[ms]) + "," + str(mm_health[mh]) + "):" + action + "=[" + str(ans1) + "]")
    return ans


def north(p, m, a, ms, mh, u, stepcost, gamma):
    # actions are down, stay, craft,
    if(mm_state[ms] == 'D'):
        p1 = 0.8
        p2 = 0.2
    else:
        p1 = 0.5
        p2 = 0.5
    ms1 = (ms+1) % 2

    t1 = stepcost + (gamma * ((p1 * ((0.85*u[1][m][a][ms][mh]) + (0.15*u[4][m][a][ms][mh]))) + (
        p2 * ((0.85*u[1][m][a][ms1][mh]) + (0.15*u[4][m][a][ms1][mh])))))
    ans = t1
    action = "DOWN"
    t2 = stepcost + (gamma * ((p1 * ((0.85*u[2][m][a][ms][mh]) + (0.15*u[4][m][a][ms][mh]))) + (
        p2 * ((0.85*u[2][m][a][ms1][mh]) + (0.15*u[4][m][a][ms1][mh])))))
    if(t2 > ans):
        ans = t2
        action = "STAY"

    if(m > 0):

        if(a + 1 < 4):
            t30 = 0.5 * ((p1*u[2][m-1][a+1][ms][mh]) +
                         (p2*u[2][m-1][a+1][ms1][mh]))
        else:
            t30 = 0.5 * ((p1*u[2][m-1][3][ms][mh]) +
                         (p2*u[2][m-1][3][ms1][mh]))

        if(a+2 < 4):
            t31 = 0.35 * ((p1*u[2][m-1][a+2][ms][mh]) +
                          (p2*u[2][m-1][a+2][ms1][mh]))
        else:
            t31 = 0.35 * ((p1*u[2][m-1][3][ms][mh]) +
                          (p2*u[2][m-1][3][ms1][mh]))

        if(a+3 < 4):
            t32 = 0.15 * ((p1*u[2][m-1][a+3][ms][mh]) +
                          (p2*u[2][m-1][a+3][ms1][mh]))
        else:
            t32 = 0.15 * ((p1*u[2][m-1][3][ms][mh]) +
                          (p2*u[2][m-1][3][ms1][mh]))

        t3 = stepcost + (gamma * (t30+t31+t32))
        if(t3 > ans):
            ans = t3
            action = "CRAFT"
    ans1 = round(ans, 3)
    print("(" + pos[p] + "," + str(mat[m]) + "," + str(arrow[a]) + "," + str(
        mm_state[ms]) + "," + str(mm_health[mh]) + "):" + action + "=[" + str(ans1) + "]")

    return ans


def south(p, m, a, ms, mh, u, stepcost, gamma):
    if(mm_state[ms] == 'D'):
        p1 = 0.8
        p2 = 0.2
    else:
        p1 = 0.5
        p2 = 0.5
    ms1 = (ms+1) % 2
    # t1 up, t2 stay, t3 for gather
    t1 = stepcost + (gamma * ((p1 * ((0.85*u[1][m][a][ms][mh]) + (0.15*u[4][m][a][ms][mh]))) + (
        p2 * ((0.85*u[1][m][a][ms1][mh]) + (0.15*u[4][m][a][ms1][mh])))))
    ans = t1
    action = "UP"
    t2 = stepcost + (gamma * ((p1 * ((0.85*u[3][m][a][ms][mh]) + (0.15*u[4][m][a][ms][mh]))) + (
        p2 * ((0.85*u[3][m][a][ms1][mh]) + (0.15*u[4][m][a][ms1][mh])))))
    if(t2 > ans):
        ans = t2
        action = "STAY"

    if(m+1 > 2):
        material = 2
    else:
        material = m+1

    t30 = (p1*u[3][material][a][ms][mh]) + (p2*u[3][material][a][ms1][mh])

    t3 = stepcost + (gamma*t30)
    if(t3 > ans):
        ans = t3
        action = "GATHER"
    ans1 = round(ans, 3)
    print("(" + pos[p] + "," + str(mat[m]) + "," + str(arrow[a]) + "," + str(
        mm_state[ms]) + "," + str(mm_health[mh]) + "):" + action + "=[" + str(ans1) + "]")
    return ans


# actons are 1) up,2) right,3) down, 4) left, 5) stay, 6) shoot,7) hit
def center(p, m, a, ms, mh, u, stepcost, gamma):
    if(mm_state[ms] == 'D'):
        # for up:
        t10 = 0.85 * ((0.2 * u[2][m][a][1][mh]) + (0.8 * u[2][m][a][0][mh]))
        t11 = 0.15 * ((0.2 * u[4][m][a][1][mh]) + (0.8 * u[4][m][a][0][mh]))
        t1 = stepcost + (gamma*(t10 + t11))
        ans = t1
        action = "UP"

        # for right:
        t20 = 0.85 * ((0.2 * u[4][m][a][1][mh]) + (0.8 * u[4][m][a][0][mh]))
        t21 = 0.15 * ((0.2 * u[4][m][a][1][mh]) + (0.8 * u[4][m][a][0][mh]))
        t2 = stepcost + (gamma*(t20 + t21))
        if(ans < t2):
            ans = t2
            action = "RIGHT"

        # for down:
        t30 = 0.85 * ((0.2 * u[3][m][a][1][mh]) + (0.8 * u[3][m][a][0][mh]))
        t31 = 0.15 * ((0.2 * u[4][m][a][1][mh]) + (0.8 * u[4][m][a][0][mh]))
        t3 = stepcost + (gamma*(t30 + t31))
        if(ans < t3):
            ans = t3
            action = "DOWN"

        # for left:
        t40 = 0.85 * ((0.2 * u[0][m][a][1][mh]) + (0.8 * u[0][m][a][0][mh]))
        t41 = 0.15 * ((0.2 * u[4][m][a][1][mh]) + (0.8 * u[4][m][a][0][mh]))
        t4 = stepcost + (gamma*(t40 + t41))
        if(ans < t4):
            ans = t4
            action = "LEFT"

        # for stay:
        t50 = 0.85 * ((0.2 * u[1][m][a][1][mh]) + (0.8 * u[1][m][a][0][mh]))
        t51 = 0.15 * ((0.2 * u[4][m][a][1][mh]) + (0.8 * u[4][m][a][0][mh]))
        t5 = stepcost + (gamma*(t50 + t51))
        if(ans < t5):
            ans = t5
            action = "STAY"

        # for shoot:
        if(a > 0):
            t60 = 0.5 * ((0.2 * u[1][m][a-1][1][mh-1]) +
                         (0.8 * u[1][m][a-1][0][mh-1]))
            t61 = 0.5 * ((0.2 * u[1][m][a-1][1][mh]) +
                         (0.8 * u[1][m][a-1][0][mh]))
            if(mh == 1):
                t6 = 25 + stepcost + (gamma * (t60 + t61))
            else:
                t6 = stepcost + (gamma * (t60 + t61))
            if(ans < t6):
                ans = t6
                action = "SHOOT"

        # for hit:
        if (mh == 1):
            rs = 0
        else:
            rs = mh-2
        t70 = 0.1 * ((0.2 * u[1][m][a][1][rs]) + (0.8 * u[1][m][a][0][rs]))
        t71 = 0.9 * ((0.2 * u[1][m][a][1][mh]) + (0.8 * u[1][m][a][0][mh]))
        if(mh <= 2):
            t7 = 5 + stepcost + (gamma * (t70 + t71))
        else:
            t7 = stepcost + (gamma * (t70 + t71))
        if(ans < t7):
            ans = t7
            action = "HIT"

    else:
        # for up:
        rx = mh+1
        if(mh >= 4):
            rx = 4
        t10 = 0.5 * u[1][m][0][0][rx]
        t11 = 0.5 * ((0.85 * u[2][m][a][1][mh]) + (0.15 * u[4][m][a][1][mh]))
        t1 = -20 + stepcost + (gamma*(t10 + t11))
        ans = t1
        action = "UP"

        # for right:
        t20 = 0.5 * u[1][m][0][0][rx]
        t21 = 0.5 * u[4][m][a][1][mh]
        t2 = -20 + stepcost + (gamma*(t20 + t21))

        if(ans < t2):
            ans = t2
            action = "RIGHT"

        # for down:
        t30 = 0.5 * u[1][m][0][0][rx]
        t31 = 0.5 * ((0.85 * u[3][m][a][1][mh]) + (0.15 * u[4][m][a][1][mh]))
        t3 = -20 + stepcost + (gamma*(t30 + t31))

        if(ans < t3):
            ans = t3
            action = "DOWN"

        # for left:
        t40 = 0.5 * u[1][m][0][0][rx]
        t41 = 0.5 * ((0.85 * u[0][m][a][1][mh]) + (0.15 * u[4][m][a][1][mh]))
        t4 = -20 + stepcost + (gamma*(t40 + t41))

        if(ans < t4):
            ans = t4
            action = "LEFT"

        # for stay:
        t50 = 0.5 * u[1][m][0][0][rx]
        t51 = 0.5 * ((0.85 * u[1][m][a][1][mh]) + (0.15 * u[4][m][a][1][mh]))
        t5 = -20 + stepcost + (gamma*(t50 + t51))

        if(ans < t5):
            ans = t5
            action = "STAY"

        # for shoot:
        if(a > 0):
            t60 = 0.5 * u[1][m][0][0][rx]
            t61 = 0.5 * ((0.5 * u[1][m][a-1][1][mh]) +
                         (0.5 * u[1][m][a-1][1][mh-1]))
            if(mh == 1):
                t6 = 12.5 - 20 + stepcost + (gamma * (t60 + t61))
            else:
                t6 = -20 + stepcost + (gamma * (t60 + t61))
            if(ans < t6):
                ans = t6
                action = "SHOOT"

        # for hit:
        if (mh == 1):
            rs = 0
        else:
            rs = mh-2
        if(mh + 1 <= 4):
            rx = mh+1
        else:
            rx = 4

        t70 = 0.5 * u[1][m][0][0][rx]
        t71 = 0.5 * ((0.9 * u[1][m][a][1][mh]) + (0.1 * u[1][m][a][1][rs]))
        if(mh <= 2):
            t7 = (0.5*-40) + (0.5*0.1*50) + stepcost + (gamma * (t70 + t71))
        else:
            t7 = (0.5 * -40) + stepcost + (gamma * (t70 + t71))
        if(ans < t7):
            ans = t7
            action = "HIT"
    ans1 = round(ans, 3)
    print("(" + pos[p] + "," + str(mat[m]) + "," + str(arrow[a]) + "," + str(
        mm_state[ms]) + "," + str(mm_health[mh]) + "):" + action + "=[" + str(ans1) + "]")
    return ans

# actons are 1) left, 2) stay, 3) shoot,4) hit


def east(p, m, a, ms, mh, u, stepcost, gamma):
    if(mm_state[ms] == 'D'):
        # left
        t10 = (0.2 * u[1][m][a][1][mh]) + (0.8 * u[1][m][a][0][mh])
        t1 = stepcost + (gamma * t10)
        ans = t1
        action = 'LEFT'
        # stay
        t20 = (0.2 * u[4][m][a][1][mh]) + (0.8 * u[4][m][a][0][mh])
        t2 = stepcost + (gamma * t20)
        if(ans < t2):
            ans = t2
            action = 'STAY'
        # shoot
        if(a > 0):
            t30 = 0.9 * ((0.2 * u[4][m][a-1][1][mh-1]) +
                         (0.8 * u[4][m][a-1][0][mh-1]))
            t31 = 0.1 * ((0.2 * u[4][m][a-1][1][mh]) +
                         (0.8 * u[4][m][a-1][0][mh]))
            t3 = stepcost + (gamma * (t30 + t31))
            if(mh == 1):
                t3 = t3 + (0.9 * 50)
            if(ans < t3):
                ans = t3
                action = 'SHOOT'
        # hit
        rs = mh-2
        if(rs < 0):
            rs = 0
        t40 = 0.2 * ((0.2 * u[4][m][a][1][rs]) + (0.8 * u[4][m][a][0][rs]))
        t41 = 0.8 * ((0.2 * u[4][m][a][1][mh]) + (0.8 * u[4][m][a][0][mh]))
        t4 = stepcost + (gamma * (t40 + t41))
        if(mh <= 2):
            t4 = t4 + (0.2 * 50)
        if(ans < t4):
            ans = t4
            action = "HIT"
    else:
        # left
        rx = mh+1
        if(rx > 4):
            rx = 4
        t10 = 0.5 * u[4][m][0][0][rx]
        t11 = 0.5 * (u[1][m][a][1][mh])
        t1 = -20 + stepcost + (gamma * (t10+t11))
        ans = t1
        action = "LEFT"

        # stay
        t20 = 0.5 * u[4][m][0][0][rx]
        t21 = 0.5 * u[4][m][a][1][mh]
        t2 = -20 + stepcost + (gamma * (t20+t21))
        if(ans < t2):
            ans = t2
            action = "STAY"

        # shoot:
        if(a > 0):
            t30 = 0.5 * u[4][m][0][0][rx]
            t31 = 0.5 * ((0.9 * u[4][m][a-1][1][mh-1]) +
                         (0.1 * u[4][m][a-1][1][mh]))
            t3 = -20 + stepcost + (gamma * (t30+t31))
            if(mh-1 <= 0):
                t3 += (0.5 * 0.9 * 50)
            if(ans < t3):
                ans = t3
                action = "SHOOT"

        # hit:
        rs = mh - 2
        if(rs < 0):
            rs = 0
        t40 = 0.5 * u[4][m][0][0][rx]
        t41 = 0.5 * ((0.2 * u[4][m][a][1][rs]) + (0.8 * u[4][m][a][1][mh]))
        t4 = -20 + stepcost + (gamma * (t40+t41))
        if(mh-2 <= 0):
            t4 += (0.5 * 0.2 * 50)
        if(ans < t4):
            ans = t4
            action = 'HIT'
    ans1 = round(ans, 3)
    print("(" + pos[p] + "," + str(mat[m]) + "," + str(arrow[a]) + "," + str(
        mm_state[ms]) + "," + str(mm_health[mh]) + "):" + action + "=[" + str(ans1) + "]")
    return ans


num_pos = 5  # W,C,N,S,E
pos = ['W', 'C', 'N', 'S', 'E']

num_mat = 3  # 0,1,2
mat = [0, 1, 2]

num_arrow = 4  # 0,1,2,3
arrow = [0, 1, 2, 3]

mm_state = ['D', 'R']  # D and R
mm_health = [0, 25, 50, 75, 100]

actions = ['up', 'down', 'left', 'right', 'stay',
           'shoot', 'hit', 'craft', 'gather', 'none']
gamma = 0.999
delta = 0.001
stepcost = -20
u = np.zeros((num_pos, num_mat, num_arrow, 2, 5))
condition = 1
iterations = 1
while(condition == 1):
    print("iteration=" + str(iterations))
    previous = np.copy(u)
    current = np.copy(u)
    for p in range(num_pos):
        for m in range(num_mat):
            for a in range(num_arrow):
                for ms in range(2):
                    for mh in range(5):
                        if(mh == 0):
                            print("(" + pos[p] + "," + str(mat[m]) + "," + str(arrow[a]) + "," + str(
                                mm_state[ms]) + "," + str(mm_health[mh]) + "):" + "NONE" + "=[" + str(0) + "]")
                            current[p][m][a][ms][mh] = 0
                            continue

                        if(pos[p] == 'W'):  # possible actions are right, stay,shoot
                            current[p][m][a][ms][mh] = west(
                                p, m, a, ms, mh, u, stepcost, gamma)

                        elif(pos[p] == 'N'):  # possible actions are down, stay, craft
                            current[p][m][a][ms][mh] = north(
                                p, m, a, ms, mh, u, stepcost, gamma)

                        elif(pos[p] == 'S'):  # possible actions are up, stay, gather
                            current[p][m][a][ms][mh] = south(
                                p, m, a, ms, mh, u, stepcost, gamma)

                        elif(pos[p] == 'C'):  # possible actions are up, stay, gather
                            current[p][m][a][ms][mh] = center(
                                p, m, a, ms, mh, u, stepcost, gamma)

                        elif(pos[p] == 'E'):  # possible actions are up, stay, gather
                            current[p][m][a][ms][mh] = east(
                                p, m, a, ms, mh, u, stepcost, gamma)

    u = np.copy(current)
    difference = np.subtract(previous, current)
    min_difference = np.min(difference)
    max_difference = np.max(difference)
    if((min_difference >= -0.001) and (max_difference <= 0.001)):
        condition = 0
    iterations += 1
