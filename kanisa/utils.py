from datetime import date, timedelta


from kanisa.models import diary
from kanisa.models import RegularEvent, ScheduledEvent


def get_week_bounds(containing=None):
    if not containing:
        containing = date.today()

    monday = containing - timedelta(days=containing.weekday())
    sunday = monday + timedelta(days=6)
    return (monday, sunday)


class DaySchedule(object):
    def __init__(self, day, thedate, regular_events, scheduled_events):
        self.date = thedate
        self.day = day
        self.dayname = diary.DAYS_OF_WEEK[day][1]
        self.scheduled_events = []

        for event in scheduled_events:
            if event.date != self.date:
                continue

            self.scheduled_events.append(event)

        self.regular_events = []

        for event in regular_events:
            if event.day != day:
                continue

            scheduled = False

            for scheduled_event in self.scheduled_events:
                if event == scheduled_event.event:
                    scheduled = True
                    break

            if scheduled:
                continue

            self.regular_events.append(event)


class WeekSchedule(object):
    def __init__(self, thedate=None):
        self.date = thedate

        if not self.date:
            self.date = date.today()

        self.monday, self.sunday = get_week_bounds(self.date)

        regular_events = RegularEvent.objects.all()
        scheduled_events = ScheduledEvent.objects.\
                                    exclude(date__lt=self.monday,
                                            date__gt=self.sunday)

        self.calendar_entries = []

        self.events_to_schedule = False

        for i in range(0, 7):
            this_date = self.monday + timedelta(days=i)
            day_schedule = DaySchedule(i,
                                       this_date,
                                       regular_events,
                                       scheduled_events)
            self.calendar_entries.append(day_schedule)

            if day_schedule.regular_events:
                self.events_to_schedule = True


def get_schedule(thedate=None):
    return WeekSchedule(thedate)
