# write an example of component test

import sys
sys.path.append('../src')

from component import Component

class TestComponent(Component):
    def __init__(self):
        Component.__init__(self)
        self.name = 'TestComponent'
        self.description = 'This is a test component'
        self.version = '0.0.1'
        self
        self.add_input('input1')
        self.add_input('input2')

    def run(self):
        print('TestComponent is running')
        print('input1 = {}'.format(self.input1))
        print('input2 = {}'.format(self.input2))

if __name__ == '__main__':
    test = TestComponent()
    test.input1 = 1
    test.input2 = 2
    test.run()
