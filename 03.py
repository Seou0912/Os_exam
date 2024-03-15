# pip3 install psutil
# 프로세서 조회
# 내 컴퓨터에서 돌아가는 프로세스 조회하기

import psutil

for proc in psutil.process_iter():

    ps_name = proc.name()

    if "Chome" in ps_name:
        print(ps_name, proc.pid)
