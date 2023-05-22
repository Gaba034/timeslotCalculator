import minuteconversor as conversor
from timerange import TimeRange
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass 
class Person(): # Creates a new Person object with the give name and busy  time range
    all_busy_minutes_range: ClassVar[list] = []
    name: str
    busy_time_range: list[TimeRange] = field(default_factory=list, repr = False)

    def add_busy_range(self, obj:TimeRange):
        self.busy_time_range.append(obj)
        Person.all_busy_minutes_range.append(obj.minutes_range)