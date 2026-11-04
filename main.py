from re import findall

logs = """
2026-10-23 10:15:32 INFO Server started
2026-10-23 10:16:01 ERROR Database connection failed
2026-10-23 10:17:45 WARNING High memory usage
2026-10-23 10:18:12 ERROR Timeout while reading request
"""

pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) ERROR (.+)"
errors = findall(pattern, logs)

for timestamp, message in errors:
    print(f"[{timestamp}] {message}")
