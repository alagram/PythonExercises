class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def print_time(self):
        print(str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))

    def __gt__(self, other):
        return (self.hours, self.minutes, self.seconds) > (other.hours, other.minutes, other.seconds)

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)


morning = Time(2, 14, 00)
afternoon = Time(13, 14, 01)

morning.print_time()
afternoon.print_time()
print(morning == afternoon)
