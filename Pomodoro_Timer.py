import time
import winsound

class PomodoroTimer:
    def __init__(self, work_minutes, break_minutes):
        self.work_minutes = work_minutes
        self.break_minutes = break_minutes

    def start_timer(self):
        print("Pomodoro Timer Started!")
        while True:
            self.work_session()
            self.break_session()

    def work_session(self):
        print(f"Work for {self.work_minutes} minutes.")
        time.sleep(self.work_minutes * 60)
        self.play_sound()

    def break_session(self):
        print(f"Take a break for {self.break_minutes} minutes.")
        time.sleep(self.break_minutes * 60)
        self.play_sound()

    def play_sound(self):
        frequency = 1500  # Hz
        duration = 1000  # milliseconds
        winsound.Beep(frequency, duration)

pomodoro_timer = PomodoroTimer(work_minutes=1, break_minutes=0.5)
pomodoro_timer.start_timer()
