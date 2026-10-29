import random
from datetime import datetime, timedelta
from collections import Counter

LOG_FILE = "application.log"
REPORT_FILE = "log_summary.txt"

random.seed(42)
levels = ["INFO", "WARNING", "ERROR"]
weights = [0.60, 0.25, 0.15]

messages = {
    "INFO": [
        "User logged in",
        "Request processed successfully",
        "File uploaded successfully",
        "User logged out",
        "Connection established"
    ],
    "WARNING": [
        "High memory usage",
        "Slow response detected",
        "Disk space running low",
        "Retrying connection"
    ],
    "ERROR": [
        "Database timeout",
        "Failed to process request",
        "Connection refused",
        "File not found",
        "Authentication failed"
    ]
}

start = datetime(2026, 7, 11, 8, 0, 0)
log_lines = []
for i in range(150):
    timestamp = start + timedelta(
        seconds=random.randint(0, 12 * 60 * 60)
    )
    level = random.choices(levels, weights=weights)[0]
    message = random.choice(messages[level])

    line = f"{timestamp:%Y-%m-%d %H:%M:%S} {level:<7} {message}"
    log_lines.append((timestamp, level, line))

log_lines.sort(key=lambda item: item[0])

with open(LOG_FILE, "w") as file:
    for timestamp, level, line in log_lines:
        file.write(line + "\n")

print(f"Generated {len(log_lines)} log entries in {LOG_FILE}")

level_counts = Counter()
error_lines = []
errors_by_hour = Counter()
with open(LOG_FILE, "r") as file:
    for line in file:
        parts = line.split(maxsplit=3)

        if len(parts) < 4:
            continue

        date_text, time_text, level, message = parts
        timestamp_text = f"{date_text} {time_text}"
        try:
            timestamp = datetime.strptime(
                timestamp_text, "%Y-%m-%d %H:%M:%S"
            )
        except ValueError:
            continue

        if level not in levels:
            continue

        level_counts[level] += 1

        if level == "ERROR":
            error_lines.append(
                f"{timestamp_text} - {message.strip()}"
            )
            errors_by_hour[timestamp.hour] += 1

if errors_by_hour:
    peak_hour, peak_count = errors_by_hour.most_common(1)[0]
    peak_result = (
        f"{peak_hour:02d}:00-{peak_hour:02d}:59 "
        f"({peak_count} errors)"
    )
else:
    peak_result = "No errors found"

report = [
    "========== LOG ANALYSIS REPORT ==========",
    f"Log file: {LOG_FILE}",
    f"Total log entries: {sum(level_counts.values())}",
    "",
    "1. LOG LEVEL COUNTS",
    "-------------------",
    f"INFO:    {level_counts['INFO']}",
    f"WARNING: {level_counts['WARNING']}",
    f"ERROR:   {level_counts['ERROR']}",
    "",
    "2. ERROR DETAILS",
    "----------------"
]

if error_lines:
    report.extend(
        f"{i}. {error}"
        for i, error in enumerate(error_lines, start=1)
    )
else:
    report.append("No errors found.")

report.extend([
    "",
    "3. PEAK ERROR HOUR",
    "------------------",
    peak_result,
    "",
    "========================================="
])

with open(REPORT_FILE, "w") as file:
    file.write("\n".join(report) + "\n")

print("\n".join(report))
print(f"Report saved to {REPORT_FILE}")

"""Log File Analyzer
Parsing logs and writing a summary report
First, programmatically generate a sample log file of 100+ lines, each looking like:

2026-07-11 09:15:32 INFO  User logged in
2026-07-11 09:16:01 ERROR Database timeout

Then parse it and report:
• the count of each log level (INFO / WARNING / ERROR)
• every ERROR line together with its timestamp
• the hour with the most errors (the peak error hour)

Finally, write the summary to a separate output file.
"""