from alarm_manager import AlarmManager
from scheduler import AlarmScheduler
from utils import validate_time

def display_menu():
    print("\n========== Alarm Clock ==========")
    print("1. Create Alarm")
    print("2. View Alarms")
    print("3. Delete Alarm")
    print("4. Exit")
    print("5. Snooze Active Alarm")
    print("=================================")


def create_alarm(manager):
    time = input("Enter alarm time (HH:MM): ").strip()

    if not validate_time(time):
        print("❌ Invalid time format.")
        return

    label = input("Enter label (optional): ").strip()

    alarm = manager.add_alarm(time, label)

    print(f"✅ Alarm created for {alarm.time}")


def view_alarms(manager):
    alarms = manager.list_alarms()

    if not alarms:
        print("No alarms found.")
        return

    print("\nSaved Alarms:")

    for i, alarm in enumerate(alarms, start=1):
        label = f" - {alarm.label}" if alarm.label else ""
        print(f"{i}. {alarm.time}{label}")


def delete_alarm(manager):
    alarms = manager.list_alarms()

    if not alarms:
        print("No alarms to delete.")
        return

    view_alarms(manager)

    try:
        choice = int(input("Enter alarm number: "))
        success = manager.delete_alarm(choice - 1)

        if success:
            print("✅ Alarm deleted.")
        else:
            print("❌ Invalid selection.")

    except ValueError:
        print("❌ Please enter a number.")


def main():
    manager = AlarmManager()

    scheduler = AlarmScheduler(manager)
    scheduler.start()

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_alarm(manager)

        elif choice == "2":
            view_alarms(manager)

        elif choice == "3":
            delete_alarm(manager)

        elif choice == "4":
            scheduler.stop()
            print("Goodbye!")
            break

        elif choice == "5":
            alarm = scheduler.active_alarm

            if alarm:
                manager.snooze_alarm(alarm.id, 5)
                scheduler.active_alarm = None
                print("Alarm snoozed for 5 minutes.")
            else:
                print("No active alarm.")

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()