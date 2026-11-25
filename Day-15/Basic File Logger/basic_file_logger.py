try:
    while True:
        log = input("Enter user action (type exit to stop): ")

        if log.lower() == "exit":
            break

        with open("user_logs.txt", "a") as file:
            file.write(log + "\n")

        print("Log saved successfully")

except OSError:
    print("File error occurred")

except Exception as e:
    print("Error:", e)
