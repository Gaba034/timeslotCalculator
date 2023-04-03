import minuteconversor as conversor
from dataclasses import dataclass, field

@dataclass
class TimeRange:
    start_time: str # 00:30
    end_time: str # 5:00

    start_minutes : int = field(init=False, repr= False)# 30
    end_minutes : int = field(init=False, repr= False)# 300
    
    def __post_init__(self):
        self.start_minutes = conversor.timerange_to_minutes(self.start_time)
        self.end_minutes = conversor.timerange_to_minutes(self.end_time)

t1 = TimeRange(start_time="00:30", end_time="05:00")
print(t1)