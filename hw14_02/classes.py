from datetime import timedelta


class Time:
    def __init__(self, *time):
        if len(time) == 1 and isinstance(time[0], str):
            self.t_hours, self.t_min, self.t_sec = map(int, time[0].split("-"))
        elif len(time) == 1 and isinstance(time[0], Time):
            self.t_hours, self.t_min, self.t_sec = time[0]
        else:
            self.t_hours, self.t_min, self.t_sec = 0, 25, 0

    def convert_to_timedelta(self):
        converted_time = timedelta(hours=self.t_hours, minutes=self.t_min, seconds=self.t_sec)
        return converted_time

    def beautiful_output(self):
        s = "{} hours {} minutes {} seconds".format(self.t_hours, self.t_min, self.t_sec)
        return s


