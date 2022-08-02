import datetime

week_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def get_schedule_for_day(serializer, day):
    """
    lesson schedule for a given day
    """
    date_time_obj = datetime.datetime.strptime(day, '%Y-%m-%d')
    week_day = date_time_obj.date().weekday()
    data = {"day": week_days[week_day], "lessons": []}
    for obj in serializer.data:
        if obj.get('day_of_week') == week_day:
            data['lessons'].append(obj)
    return data


def get_schedule_for_week(serializer):
    """
    lesson schedule for the thole week
    """
    lesson_schedule = [{"day": v, "lessons": []} for v in week_days.values()]
    i = 0
    for k, v in week_days.items():
        for obj in serializer.data:
            if obj.get('day_of_week') == k:
                lesson_schedule[i]['lessons'].append(obj)
        i += 1
    return lesson_schedule
