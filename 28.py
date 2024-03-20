# 파일 복사 또는 이동

import os
import shutil

pwd = "/Users/seou_mac15/Desktop/Seou/os-exam/Os_exam/project"
filenames = os.listdir(pwd)

for filename in filenames:
    if "something" in filename:
        origin = os.path.join(pwd, filename)
        print(origin)
        # shutil.copy(origin, os.path.join(pwd, "copy.txt"))  # 복사
        shutil.move(origin, os.path.join(pwd, "anony"))
