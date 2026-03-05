# 1번 문제

from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "TEST"
DATA_DIR.mkdir(parents=True, exist_ok=True)

def logs():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H-%M-%S")

    t = input("로그 내용을 입력해주세요 : ")
    file_name = f"{timestamp}  {t}.txt"
    logs_path = DATA_DIR / file_name

    # 쓰기 모드(이어쓰기)
    f = open(logs_path, "a", encoding="utf-8")
    f.write(f"{t}\n")
    f.close()

    # 읽기 모드
    f = open(logs_path, "r", encoding="utf-8")
    content = f.read()
    f.close()

    print("[content]:", content)

if __name__ == "__main__":
    logs()