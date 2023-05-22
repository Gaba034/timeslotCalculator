import minuteconversor as conversor
from dataclasses import dataclass, field

@dataclass
class TimeRange: # Creates a TimeRange object with the specified range
    start_time: str # 00:30
    end_time: str # 5:00
    start_minutes : int = field(init=False, repr= False)# 30
    end_minutes : int = field(init=False, repr= False)# 300
    minutes_range: range = field(init=False, repr= False)
    def __post_init__(self):
        self.start_minutes = conversor.timerange_to_minutes(self.start_time)
        self.end_minutes = conversor.timerange_to_minutes(self.end_time)
        self.minutes_range = range(self.start_minutes, self.end_minutes, 1)