class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class StateMachine:
    state = 'A'

    def fill(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        elif self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise(MealyError('fill'))

    def order(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'F':
            self.state = 'D'
            return 8
        else:
            raise(MealyError('order'))

    def log(self):
        if self.state == 'A':
            self.state = 'D'
            return 2
        elif self.state == 'B':
            self.state = 'C'
            return 3
        elif self.state == 'C':
            self.state = 'A'
            return 5
        else:
            raise(MealyError('log'))


def main():
    return StateMachine()


def test():
    test_exceptions = [
        ('B', 'order'),
        ('B', 'fill'),
        ('C', 'fill'),
        ('D', 'log'),
        ('D', 'fill'),
        ('E', 'log'),
        ('E', 'order'),
        ('F', 'log'),
        ('F', 'fill')
    ]

    test_result = [
        ('A', 'fill', 1, 'A'),
        ('A', 'log', 2, 'D'),
        ('A', 'order', 0, 'B'),
        ('B', 'log', 3, 'C'),
        ('C', 'log', 5, 'A'),
        ('C', 'order', 4, 'D'),
        ('D', 'order', 6, 'E'),
        ('E', 'fill', 7, 'F'),
        ('F', 'order', 8, 'D')
    ]
    sm = main()
    for start_state, action in test_exceptions:
        sm.state = start_state
        try:
            if action == 'fill':
                sm.fill()
            elif action == 'log':
                sm.log()
            else:
                sm.order()
        except MealyError:
            pass
    for start_state, action, expected_return, expected_state in test_result:
        sm.state = start_state
        if action == 'fill':
            assert sm.fill() == expected_return
            assert sm.state == expected_state
        elif action == 'log':
            assert sm.log() == expected_return
            assert sm.state == expected_state
        else:
            assert sm.order() == expected_return
            assert sm.state == expected_state
