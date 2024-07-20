from collections import Counter
import sys


def parse_log_line(line: str) -> dict:
    date, time, level, *words = line.strip().split(" ")
    return {
        "raw_line": line,
        "date": date,
        "time": time,
        "level": level,
        "message": " ".join(words),
    }


def load_logs(file_path: str) -> list:
    logs_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            for line in fh.readlines():
                logs_list.append(parse_log_line(line))
    except Exception:
        print("File error")
        sys.exit()
        

    return logs_list


def filter_logs_by_level(logs: list, level: str) -> list:
    return filter(lambda log: log["level"] == level, logs)


def count_logs_by_level(logs: list) -> dict:
    levels = [log["level"] for log in logs]
    return Counter(levels)


def display_log_counts(counts: dict, input_level: str):
    level_title = "Level"
    amount_title = "Amount"
    print(f"{level_title:^10}|{amount_title:^10}")
    print("-" * 21)

    for level, count in counts.items():
        is_active = input_level == level
        print(f'{">" if is_active else " "}{level:^9}|{count:^10}')


def main():
    _, file_path, *_ = sys.argv

    input_level = ""
    try:
        input_level = sys.argv[2].upper()
    except:
        pass

    logs = load_logs(file_path)

    log_counts = count_logs_by_level(logs)

    display_log_counts(log_counts, input_level)

    if input_level:
        level_logs = filter_logs_by_level(logs, input_level)
        for log in level_logs:
            print(log["raw_line"].strip())


if __name__ == "__main__":
    main()
