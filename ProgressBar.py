class ProgressBar:

    def __init__(self, max_value, start_value=0):
        self.value = start_value
        self.max_value = max_value
        self.show_fraction = False
        self.bar_length = 10

    def display(self, newline=False):

        if self.value > self.max_value:
            self.value = self.max_value
        elif self.value < 0:
            self.value = 0

        percentage = 100 * self.value / self.max_value
        full = int(percentage * self.bar_length / 100)
        empty = self.bar_length - full

        percentage = int(percentage)

        if self.show_fraction:
            percentage = f"{percentage}% ({self.value}/{self.max_value})"
        else:
            percentage = f"{percentage}%"

        if not newline:
            print("[" + ("#" * full) + ("-" * empty) + "] {}\r".format(percentage), end="")
        else:
            print("[" + ("#" * full) + ("-" * empty) + "] {}".format(percentage))

        if self.is_finished() and not newline:
            print("\n")

    def increment(self, value=1):
        self.value += value

    def is_finished(self):
        return self.value >= self.max_value


