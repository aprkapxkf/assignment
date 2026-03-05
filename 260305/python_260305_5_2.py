# 2번 문제

from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "TEST"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def logs():

    t = input("로그 내용을 입력해주세요 : ")
    file_name = "students.txt"
    logs_path = DATA_DIR / file_name

    rows = [
        ("2025-01-03", "식비", "김밥", "card", 3500, "점심"),
        ("2025-01-04", "교통", "버스", "card", 1500, "출근"),
        ("2025-01-05", "통신", "휴대폰", "acct", 30000, "12월")
    ]

    with open(file_name, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "item", "method", "amount", "note"])
        writer.writerows(rows)
    
    #읽기
    total = 0
    with open(file_name, "r", encoding="utf-8", newline="") as f:
        dr = csv.DictReader(f)
        for row in dr:
            print(row)
            total += int(row["amount"])

    print(f"총 합계: {total}")