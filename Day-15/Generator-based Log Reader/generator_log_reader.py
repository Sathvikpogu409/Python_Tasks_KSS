def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


error_count = {}

try:
    for log in read_logs("system_logs.txt"):

        if "ERROR" in log:
            print(log)

            error_count["ERROR"] = error_count.get("ERROR", 0) + 1

    print("Error Count:", error_count)

except FileNotFoundError:
    print("Log file not found")
