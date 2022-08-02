from django.db.models import Model, CharField, ManyToManyField,\
    ForeignKey, PROTECT, CASCADE, IntegerField

from references.models import Subject, Room, Groups, Pair
from users.models.user import User


class Lesson(Model):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5

    week_days = (
        (Monday, 'MONDAY'),
        (Tuesday, 'TUESDAY'),
        (Wednesday, 'WEDNESDAY'),
        (Thursday, 'THURSDAY'),
        (Friday, 'FRIDAY'),
        (Saturday, 'SATURDAY'),
    )

    subject = ForeignKey(Subject, PROTECT, 'subject_lessons')
    room = ForeignKey(Room, PROTECT, 'room_lessons')
    group = ForeignKey(Groups, CASCADE, 'group_lessons')
    teacher = ForeignKey(User, PROTECT, 'teacher_lessons')
    day_of_week = IntegerField(choices=week_days)
    pair = ForeignKey(Pair, PROTECT, 'pair_lessons')

    def __str__(self):
        return str(self.id)
