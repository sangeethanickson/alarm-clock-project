# ⏰ Python CLI Alarm Clock

A lightweight command-line alarm clock application built in Python. The application allows users to create, view, delete, and snooze alarms while running entirely in the terminal.

The project was intentionally designed with a minimal specification to demonstrate requirement analysis, engineering decision-making, and incremental feature development.

---

# Features

* Create alarms with a time and optional label
* View all saved alarms
* Delete existing alarms
* Background scheduler that checks alarms continuously
* Desktop notifications using `plyer`
* Snooze active alarms for 5 minutes
* Persistent storage using JSON
* Modular and extensible architecture

---

# Requirement Analysis

The exercise intentionally did not provide a detailed specification. Therefore, the following assumptions were made:

## Functional Requirements

* Users should be able to create alarms.
* Users should be able to view alarms.
* Users should be able to delete alarms.
* Multiple alarms should be supported.
* Alarms should trigger at the specified time.
* Users should be able to snooze active alarms.

## Non-Functional Requirements

* The application should run entirely in the terminal.
* The application should not require a database.
* The application should use minimal dependencies.
* The solution should be easy to maintain and extend.
* Alarm checking should not block the user interface.

---

# Assumptions

* Minute-level precision is sufficient for an alarm clock MVP.
* One-time alarms are sufficient for the initial implementation.
* JSON file storage is adequate instead of a database.
* Desktop notifications improve usability when the terminal is not focused.

---

# Architecture

Main Thread
    │
    ├── CLI Menu
    │
    └── AlarmManager
            │
            └── alarms.json

Background Thread
    │
    └── AlarmScheduler
            │
            ├── Checks alarms every second
            ├── Prints alarm message
            └── Sends desktop notification


# Project Structure

alarm-clock/
│
├── main.py
├── alarm_manager.py
├── scheduler.py
├── models.py
├── utils.py
├── alarms.json
├── requirements.txt
├── README.md
└── .gitignore

---

# Design Decisions

## Why JSON instead of a database?

The assignment explicitly mentioned that a database was unnecessary. JSON was chosen because:

* Zero setup
* Human readable
* Easy persistence
* Suitable for a small CLI application

---

## Why use threading?

The scheduler continuously checks alarm times. Running this logic in the main thread would block the CLI.

A background daemon thread allows:

* Alarm checking in parallel
* Responsive user interface
* Clear separation of concerns

---

## Why avoid user input inside the scheduler thread?

The scheduler and CLI both require terminal input.

Reading from `stdin` in multiple threads causes race conditions and inconsistent behavior.

Therefore:

* User interaction remains in the main thread.
* Alarm events are communicated through shared state.

This keeps the implementation simple and avoids thread contention.

---

## Why desktop notifications?

A terminal-only alarm is easy to miss when another application is in focus.

Desktop notifications were added using the `plyer` library to improve usability.

Terminal output remains the primary alarm mechanism, while notifications are treated as a best-effort enhancement.

---

# Snooze Functionality

The application supports snoozing active alarms.

Implementation approach:

* The existing alarm's scheduled time is updated.
* A new alarm object is not created.
* The updated alarm is persisted to JSON.

This keeps the data model simple and avoids duplicate alarms.

---

# How to Run

## Clone the repository

git clone https://github.com/sangeethanickson/alarm-clock-project.git
cd alarm-clock

## Create virtual environment

### Windows

python -m venv venv
venv\Scripts\activate

### Linux / Mac

python3 -m venv venv
source venv/bin/activate

---

## Install dependencies

pip install -r requirements.txt

---

## Start the application

python main.py

---

# Example Usage

========== Alarm Clock ==========
1. Create Alarm
2. View Alarms
3. Delete Alarm
4. Exit
5. Snooze Active Alarm
=================================

---

# Example Alarm

Enter alarm time (HH:MM): 09:30
Enter label (optional): Interview

When the alarm triggers:

🔔 ALARM! 09:30 - Interview

A desktop notification is also displayed.

---

# Edge Cases Considered

* Invalid time formats
* Empty alarm list
* Invalid delete selections
* Multiple alarms at the same time
* Persistence across application restarts
* Scheduler running concurrently with the CLI

---

# Future Improvements

* Recurring alarms
* Custom snooze durations
* Sound notifications
* Time zone support
* Alarm editing
* Unit and integration tests
* Cross-platform desktop notification improvements

---

# AI Usage

AI tools were used to:

* Refine requirements from an intentionally ambiguous specification.
* Explore architectural approaches.
* Identify concurrency concerns.
* Review implementation tradeoffs.

All generated suggestions were manually reviewed, adapted, and validated during implementation.

---

# Technologies Used

* Python 3.16
* threading
* datetime
* json
* uuid
* plyer

---

# Tradeoffs

* Chose simplicity over feature completeness.
* Preferred standard library modules wherever possible.
* Implemented an MVP first and added enhancements incrementally.
* Optimized for maintainability and clarity rather than over-engineering.