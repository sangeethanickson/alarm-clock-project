import threading
import time
from datetime import datetime
from plyer import notification

class AlarmScheduler:
    def __init__(self, alarm_manager):
        self.alarm_manager = alarm_manager
        self.running = True
        self.triggered = set()
        self.active_alarm = None

    def check_alarms(self):
        while self.running:
            current_time = datetime.now().strftime("%H:%M")

            for alarm in self.alarm_manager.list_alarms():
                key = f"{alarm.id}-{current_time}"

                if (
                    alarm.active
                    and alarm.time == current_time
                    and key not in self.triggered
                ):
                    
                    notification.notify(
                        title="Alarm Clock",
                        message=f"🔔 {alarm.label or 'Alarm'}",
                        timeout=10
                    )
                    print(f"\n🔔 ALARM! {alarm.time}")
                    print("Use option 5 from the menu to snooze this alarm.")

                    self.active_alarm = alarm
                    self.triggered.add(key)

            time.sleep(1)

    def start(self):
        thread = threading.Thread(
            target=self.check_alarms,
            daemon=True
        )
        thread.start()

    def stop(self):
        self.running = False