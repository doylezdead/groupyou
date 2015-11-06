from groupyou.job import Job


class Date(Job):
    def __init__(self):
        super(Job, self).__init__()

    def trigger(self, minuteofhour, hourofday, dayofweek, dayofmonth, dayofyear):
        return False
