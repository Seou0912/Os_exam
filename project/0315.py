import os
import psutil


def find_process_name_by_pid(target_pid):
    # 모든 실행 중인 프로세스에 대해 반복
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        # 현재 프로세스의 PID가 목표 PID와 일치하는지 확인
        if proc.info["pid"] == target_pid:
            # 일치한다면 프로세스의 이름을 반환
            return proc.info["name"]
    # 일치하는 프로세스를 찾지 못한 경우
    return None


# 현재 파이썬 스크립트의 PID를 얻음
current_pid = os.getpid()
# 해당 PID를 가진 프로세스의 이름을 찾음
process_name = find_process_name_by_pid(current_pid)

if process_name:
    print(f"현재 스크립트의 프로세스 이름: {process_name}")
else:
    print("프로세스를 찾을 수 없습니다.")
