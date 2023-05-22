import minuteconversor as h
from timerange import TimeRange
from person import Person
from customized_list import CustomList

def main():
    available_time = CustomList(range(1440))
    person1 = Person("Tom")
    person1.add_busy_range(TimeRange(start_time="08:00",end_time="12:00"))
    person2 = Person("Bob")
    person2.add_busy_range(TimeRange(start_time="08:00",end_time="17:00"))
    person3= Person("Mike")
    person3.add_busy_range(TimeRange(start_time="12:00",end_time="20:30"))
    for time in available_time[:]:
        for r in Person.all_busy_minutes_range:
            if time in r:
                available_time.remove_if_exist(time)
    for tr in h.enhance_time_display(available_time):
        print(f"Vocês podem se encontrar às {tr}")
        
if __name__ == '__main__':
    main()