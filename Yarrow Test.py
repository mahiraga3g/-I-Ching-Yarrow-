dayan = 50
#大衍之数五十

qiyong = 49
#其用四十有九

import random
lefthand = random.randint(1, 48)
#49根筹策分成左右两部分
righthand = qiyong - lefthand
#右边的份数
rightyong = righthand - 1
#右边份数减一


leftyushu = lefthand % 4
if leftyushu == 0:
    leftyushuyi = 4
elif leftyushu > 0:
    leftyushuyi = leftyushu


rightyushu = rightyong % 4
if rightyushu == 0:
    rightyushuyi = 4
elif rightyushu > 0:
    rightyushuyi = rightyushu

diyibian = leftyushuyi + rightyushuyi + 1
#得出第一变，第一变不是五就是九
yibianhou = qiyong - diyibian
print(yibianhou)
#第一变后筹策数不是四十四就是四十

lefthander = random.randint(1, yibianhou - 1)
righthander = yibianhou - lefthander
rheyong = righthander - 1


leftyushub = lefthander % 4
if leftyushub == 0:
    leftyushuer = 4
elif leftyushub > 0:
    leftyushuer = leftyushub


rightyushub = rheyong % 4
if rightyushub == 0:
    rightyushuer = 4
elif rightyushub > 0:
    rightyushuer = rightyushub

erbian = leftyushuer + rightyushuer + 1

erbianhou = yibianhou - erbian
print(erbianhou)

lefthandsan = random.randint(1, erbianhou - 1)
print(lefthandsan)
righthandsan = erbianhou - lefthandsan
print(righthandsan)
rhys = righthandsan - 1
print(rhys)


leftyushuc = lefthandsan % 4
if leftyushuc == 0:
        leftyushusan = 4
elif leftyushuc > 0:
        leftyushusan = leftyushuc

rightyushuc = rhys % 4
if rightyushuc == 0:
        rightyushusan = 4
elif rightyushuc > 0:
        rightyushusan = rightyushuc
print(leftyushusan)
print(rightyushusan)

sanbian = leftyushusan + rightyushusan + 1
sanbianhou = erbianhou - sanbian
print(sanbianhou)