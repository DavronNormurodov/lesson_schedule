from django.db.models import Model, CharField, ManyToManyField, \
    IntegerField, TimeField


class Subject(Model):
    title = CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)


class Room(Model):
    title = CharField(max_length=155)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)


class Groups(Model):
    title = CharField(max_length=155)
    students = ManyToManyField('users.User', blank=True, related_name='student_groups')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)


class Pair(Model):
    index = IntegerField(unique=True)
    start_time = TimeField()
    end_time = TimeField()

    def __str__(self):
        return str(self.index)

    class Meta:
        ordering = ('index', )
