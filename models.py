from dataclasses import dataclass, asdict

@dataclass
class Alarm:
    id: str
    time: str
    label: str
    active: bool = True
    snooze_count: int = 0

    def to_dict(self):
        return asdict(self)