def timerange_to_minutes(t_str):
    """
    Return amount of minutes for timeranges in format HH:MM
    :param t_str:
    :return:    
    
    """
    # 05:00
    hour = int(t_str.split(':')[0])
    minutes = int(t_str.split(':')[1])
    hour_to_minutes = hour * 60
    return hour_to_minutes + minutes

def minutes_to_timerange_str(m):
    """
        Converts the minutos to a timerange string.
    """
    hour = m // 60
    minutes = m % 60
    timestring = f'{hour:02d}:{minutes:02d}'
    print(timestring)

def enhance_time_display():
    l = [0,1,2,3,60,61,62]
    agrouped_list = []
    reusable_list = []

    for element in l:
        if reusable_list == []:
            reusable_list.append(element)
            continue
        if reusable_list[-1] + 1 == element:
            reusable_list.append(element)
        else:
            agrouped_list.append(reusable_list[:])
            reusable_list.clear()
            reusable_list.append(element)

    agrouped_list.append(reusable_list)
    print(agrouped_list)


enhance_time_display()
minutes_to_timerange_str(m = 519)