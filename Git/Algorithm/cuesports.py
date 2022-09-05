import math

# 직선과 점 사이의 거리 
def cal_dist(x1, y1, x2, y2, a, b):
    area = abs((x1-a) * (y2-b) - (y1-b) * (x2 - a))
    AB = ((x1-x2)**2 + (y1-y2)**2) **0.5
    distance = area/AB
    return distance

# 수구 위치 찾기 (x, y라고 가정)
myball_x = 'x'
myball_y = 'y'

# 선공, 후공 판단
#order 1이면 1, 3, 5 공 넣기
if order == 1:
    target_num = [1, 3, 5]
else:
    target_num = [2, 4, 5]

# 공들 순회하면서 목적구의 X, Y좌표 찾기
for i in target_num:
    if balls[i][0] != -1:
        targetBall_x = balls[i][0]
        targetBall_y = balls[i][1]
        break

# 수구와 목적구의 상하관계를 판단해 어느쪽 홀을 기준으로 넣을지 판단
if myball_y > targetBall_y:
    hole_num = [0, 1, 2]
else:
    hole_num = [3, 4, 5]
    
# 칠 수 있는 방향에 있는 홀 찾기
for i in hole_num:
    hx = HOLES[i][0]
    hy = HOLES[i][1]
    if hx <= targetBall_x <= myball_x or myball_x <= targetBall_x <= hx:
        target_hole = HOLES[i]
    
# 타겟으로 한 홀과 목적구의 각도 찾기
hx = target_hole[0]
hy = target_hole[1]
tx = targetBall_x
ty = targetBall_y
y = abs(hy - ty)
x = abs(hx - tx)
z = math.sqrt((abs(hx-tx)**2) + (abs(hy-ty)**2))
degree = math.atan2(y, x)

# 닮음 이용해서 가상구 위치 찾기
pz = z + 5.74
px = math.cos(degree) * pz
py = math.sin(degree) * pz
if hx > tx and hy > ty:
    targetBall_x, targetBall_y = hx-px, hy-py
elif hx < tx and hy > ty:
    targetBall_x, targetBall_y = hx+px, hy-py
elif hx < tx and hy < ty:
    targetBall_x, targetBall_y = hx+px, hy+py
elif hx > tx and hy < ty:
    targetBall_x, targetBall_y = hx-px, hy+py

# 두 점사이 거리
distance = math.sqrt(width**2 + height**2)

# 가는 길 안에 상대방 공 체크
for i in range(1, 5):
    if balls[i][0] != -1 and i not in target_num:
        if 5.74 > cal_dist(targetBall_x, targetBall_y, myball_x, myball_y, balls[i][0], balls[i][1]):
# 있다면, 검은공을 약하게 친다. => 파울 최소화
            targetBall_x = balls[5][0]
            targetBall_y = balls[5][1]
            power = distance * 0.3
            break

# 없으면, 거리 distance에 따른 힘의 세기를 계산
else:
    power = distance * 0.73035

# width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
width = abs(targetBall_x - myball_x)
height = abs(targetBall_y - myball_y)

# 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 계산
if myball_x <= targetBall_x and myball_y < targetBall_y:
    radian = math.atan(width / height)
    angle = 180 / math.pi * radian

# 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
elif myball_x > targetBall_x and myball_y < targetBall_y:
    radian = math.atan(width / height)
    angle = 90 - (180 / math.pi * radian) + 270

# 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
elif myball_x >= targetBall_x and myball_y >= targetBall_y:
    radian = math.atan(width / height)
    angle = (180 / math.pi * radian) + 180
    
# 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
elif myball_x <= targetBall_x and myball_y >= targetBall_y:
    radian = math.atan(height / width)
    angle = (180 / math.pi * radian) + 90