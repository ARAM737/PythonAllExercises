class C32:
    def __init__(self):
        self.state = 'A'

    def etch(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise RuntimeError

    def click(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'G':
            self.state = 'E'
            return 9
        else:
            raise RuntimeError

    def brake(self):
        if self.state == 'A':
            self.state = 'D'
            return 2
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise RuntimeError