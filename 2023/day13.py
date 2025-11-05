import time
import numpy as np


def get_score(m, part=False):
    m = np.array([np.array([*x]) for x in m])
    m = m == '#'
    # searching columns first
    for i in range(1, m.shape[1]):
        # left slice
        m_l = m[:, 0:i]
        # right slice
        m_r = m[:, i:]
        # find the min width
        w = min(m_l.shape[1], m_r.shape[1])
        # reduce left and right to the same wide
        m_l = m_l[:, -w:]
        m_r = m_r[:, :w]
        # flip the right side
        m_r = m_r[:, ::-1]
        if not part:
            if (m_l == m_r).all():
                return i
        else:
            if (~(m_l == m_r)).sum() == 1:
                return i
    for i in range(1, m.shape[0]):
        m_u = m[0:i]
        m_d = m[i:]
        h = min(m_u.shape[0], m_d.shape[0])
        m_u = m_u[-h:]
        m_d = m_d[:h]
        m_d = m_d[::-1]
        if not part:
            if (m_u == m_d).all():
                return i * 100
        else:
            if (~(m_u == m_d)).sum() == 1:
                return i * 100
    return 0


start_time = time.time()
f = open('input13.txt')
data = [[line.strip() for line in group.split('\n')] for group in f.read().split('\n\n')]
score = 0
for m in data:
        score += get_score(m)
pt1 = score
score = 0
for m in data:
        score += get_score(m,True)
pt2 = score

# pt2 = get_score(data, True)
print(pt1, pt2)
print("--- %s seconds ---" % (time.time() - start_time))
