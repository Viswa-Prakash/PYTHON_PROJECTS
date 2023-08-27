import time

alarm_time = input("Enter the alarm time in HH:MM format: ")

while True:
    current_time = time.strftime("%H:%M")

    if current_time == alarm_time:
        print("Time to wake up")
        break
    else:
        print(f"current_time: {current_time}")
        time.sleep(60)
