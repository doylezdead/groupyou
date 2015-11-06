from groupyou.job import Job


class Date(Job):

    def trigger(self, minuteofhour, hourofday, dayofweek, dayofmonth, dayofyear):
        return False
