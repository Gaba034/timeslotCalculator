from timerange import TimeRange
from person import Person

def main():
    
    available_time = list(range(1440))
    person1 = Person("Tom")
    person1.add_busy_range(TimeRange(start_time="08:00",end_time="12:00"))
    person2 = Person("Bob")
    person2.add_busy_range(TimeRange(start_time="13:00",end_time="17:00"))
    
    for time in available_time[:]:
        for r in Person.all_busy_minutes_range:
            if time in r:
                available_time.remove(time)
    print(available_time)

if __name__ == '__main__':
    main()