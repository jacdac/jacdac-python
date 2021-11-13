import functools
import heapq
from . import util

class TaskQ:
    def __init__(self) -> None:
        self.tasks: list['ProcessTask'] = []

    def _toptask(self):
        if len(self.tasks):
            return self.tasks[0]
        return None

    def execute(self):
        while True:
            n = util.now()
            t = self._toptask()
            if t.when > n:
                break
            t2 = heapq.heappop(self.tasks)
            assert t is t2
            if t.repeat:
                t.when += t.repeat
                heapq.heappush(self.tasks, t)
            t.fn()

    def sleeptime(self):
        d = 100
        t = self._toptask()
        if t:
            d = t.when - util.now()
            if d < 0:
                d = 0
        return d

    def delay(self, delta_ms: int, fn: callable[[], None]):
        heapq.heappush(self.tasks, ProcessTask(util.now() + delta_ms, fn))

    def recurring(self, delta_ms: int, fn: callable[[], None]):
        t = ProcessTask(util.now() + delta_ms, fn)
        t.repeat = delta_ms
        heapq.heappush(self.tasks, t)


@functools.total_ordering
class ProcessTask:
    def __init__(self, when: int, fn: callable[[], None]) -> None:
        self.when = when
        self.fn = fn
        self.repeat = 0

    def __lt__(self, other: 'ProcessTask'):
        return self.when < other.when
