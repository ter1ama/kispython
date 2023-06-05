class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class StateMachine:
    state = 'A'

    def click(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'D'
            return 3
        elif self.state == 'C':
            self.state = 'G'
            return 5
        elif self.state == 'D':
            self.state = 'F'
            return 7
        else:
            raise (MealyError('click'))

    def pan(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        elif self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'F':
            self.state = 'G'
            return 9
        elif self.state == 'H':
            self.state = 'E'
            return 11
        else:
            raise (MealyError('pan'))

    def split(self):
        if self.state == 'C':
            self.state = 'D'
            return 4
        else:
            raise (MealyError('split'))

    def get(self):
        if self.state == 'E':
            self.state = 'F'
            return 8
        elif self.state == 'G':
            self.state = 'H'
            return 10
        else:
            raise (MealyError('get'))


def main():
    return StateMachine()


def test():
    test_exceptions = [
        ('A', 'get'),
        ('A', 'split'),
        ('B', 'get'),
        ('B', 'split'),
        ('C', 'get'),
        ('C', 'pan'),
        ('D', 'get'),
        ('D', 'split'),
        ('E', 'pan'),
        ('E', 'split'),
        ('E', 'click'),
        ('F', 'click'),
        ('F', 'pan'),
        ('F', 'get'),
        ('G', 'pan'),
        ('G', 'click'),
        ('G', 'split'),
        ('H', 'split'),
        ('H', 'get'),
        ('H', 'click'),
    ]
    test_result = [
        ('A', 'click', 0, 'B'),
        ('A', 'pan', 1, 'C'),
        ('B', 'pan', 2, 'C'),
        ('B', 'click', 3, 'D'),
        ('C', 'split', 4, 'D'),
        ('C', 'click', 5, 'G'),
        ('D', 'pan', 6, 'E'),
        ('D', 'click', 7, 'F'),
        ('E', 'get', 8, 'F'),
        ('F', 'pan', 9, 'G'),
        ('G', 'get', 10, 'H'),
        ('H', 'pan', 11, 'E'),
    ]
    sm = main()
    for start_state, action in test_exceptions:
        sm.state = start_state
        try:
            if action == 'click':
                sm.click()
            elif action == 'split':
                sm.split()
            elif action == 'pan':
                sm.pan()
            else:
                sm.get()
        except MealyError:
            pass
    for start_state, action, expected_return, expected_state in test_result:
        sm.state = start_state
        if action == 'click':
            assert sm.click() == expected_return
            assert sm.state == expected_state
        elif action == 'split':
            assert sm.split() == expected_return
            assert sm.state == expected_state
        elif action == 'pan':
            assert sm.pan() == expected_return
            assert sm.state == expected_state
        else:
            assert sm.get() == expected_return
            assert sm.state == expected_state
