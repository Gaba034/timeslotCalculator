import minuteconversor as conversor
from timerange import TimeRange
from dataclasses import dataclass, field

@dataclass
class Person():
    name: str
    busy_time_range: list[TimeRange] = field(default_factory=list, repr = False)

    def add_busy_range(self, obj:TimeRange):
        self.busy_time_range.append(obj)


f1 = Person('Tom')
f1.add_busy_range(TimeRange(start_time="09:00",end_time="16:30"))
print(f1.busy_time_range)