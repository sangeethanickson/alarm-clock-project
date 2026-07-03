import json
import os
import uuid

from models import Alarm
from datetime import datetime, timedelta

class AlarmManager:
    def __init__(self, file_name="alarms.json"):
        self.file_name = file_name
        self.alarms = []
        self.load_alarms()

    def load_alarms(self):
        if not os.path.exists(self.file_name):
            return

        try:
            with open(self.file_name, "r") as file:
                data = json.load(file)

            self.alarms = [
                Alarm(**alarm)
                for alarm in data
            ]
        except Exception:
            self.alarms = []

    def save_alarms(self):
        with open(self.file_name, "w") as file:
            json.dump(
                [alarm.to_dict() for alarm in self.alarms],
                file,
                indent=4
            )

    def add_alarm(self, time, label=""):
        alarm = Alarm(
            id=str(uuid.uuid4()),
            time=time,
            label=label
        )

        self.alarms.append(alarm)
        self.save_alarms()
        return alarm

    def list_alarms(self):
        return self.alarms

    def delete_alarm(self, index):
        if index < 0 or index >= len(self.alarms):
            return False

        self.alarms.pop(index)
        self.save_alarms()
        return True
    
    def snooze_alarm(self, alarm_id, minutes=5):
        for alarm in self.alarms:
            if alarm.id == alarm_id:
                current = datetime.strptime(alarm.time, "%H:%M")
                new_time = current + timedelta(minutes=minutes)

                alarm.time = new_time.strftime("%H:%M")
                self.save_alarms()

                return alarm

        return None