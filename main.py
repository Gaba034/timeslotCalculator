from timerange import TimeRange
from person import Person

def main():
    available_time = list(range(1440))
    person1 = Person("Tom")
    person1.add_busy_range(TimeRange(start_time="08:00",end_time="18:00"))
    person2 = Person("Bob")
    person2.add_busy_range(TimeRange(start_time="10:00",end_time="14:00"))
    
    for time in available_time[:]:
        if time in person1.busy_time_range[0].minutes_range:
            available_time.remove(time)
    print(available_time)

if __name__ == '__main__':
    main()