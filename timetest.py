import time
from timeout import timeout

class Test(object):
    @timeout(2)
    def test_a(self, foo, bar):
        print(foo)
        time.sleep(1)
        print(bar)
        return 'A Done'

    @timeout(2)
    def test_b(self, foo, bar):
        print(foo)
        time.sleep(3)
        print(bar)
        return 'B Done'

t = Test()
print(t.test_a('python', 'rocks'))
print(t.test_b('timing', 'out'))