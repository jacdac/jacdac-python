import threading
from typing import Any, Callable, TYPE_CHECKING, Coroutine, Union

if TYPE_CHECKING:
    from .bus import Bus

HandlerFn = Callable[..., Union[None, Coroutine[Any, Any, None]]]


class EventEmitter:
    def __init__(self, bus: 'Bus') -> None:
        self.bus = bus

    def emit(self, id: str, *args: object):
        def add_cb(fn: HandlerFn):
            def cb():
                r = fn(*args)
                if r is None:
                    return
                # print(r)
                t = self.bus.loop.create_task(r)
                self.bus.pending_tasks.append(t)
                # print(t)
            self.bus.loop.call_soon(cb)

        self.bus.force_jd_thread()
        if not hasattr(self, "_listeners"):
            return
        idx = 0
        while idx < len(self._listeners):
            lid, fn, once = self._listeners[idx]
            if lid == id:
                # note that add_cb() can't be inlined here due to lack of block scope in Python
                add_cb(fn)
                if once:
                    del self._listeners[idx]
                    idx -= 1
            idx += 1

    def _init_emitter(self):
        if not hasattr(self, "_listeners"):
            self._listeners: list[tuple[str, HandlerFn, bool]] = []

    def on(self, id: str, fn: HandlerFn):
        # Subscribes an event to a handler
        self._init_emitter()
        self._listeners.append((id, fn, False))

    def once(self, id: str, fn: HandlerFn):
        # Subsubscribes an event to run once; then get unsubscribed
        self._init_emitter()
        self._listeners.append((id, fn, True))

    def off(self, id: str, fn: HandlerFn):
        # Unsubscribes a handler from an event
        self._init_emitter()
        for i in range(len(self._listeners)):
            id2, fn2, _ign = self._listeners[i]
            if id == id2 and fn is fn2:
                del self._listeners[i]
                return
        raise ValueError("no matching on() for off()")

    def subscribe(self, id: str, fn: HandlerFn):
        # Subscribes a handler to the event and returns a function to unsubscribe
        self.on(id, fn)

        def unsubscribe():
            return self.off(id, fn)
        return unsubscribe

    # usage: await x.event("...")
    async def event(self, id: str):
        f = self.bus.loop.create_future()
        self.once(id, lambda: f.set_result(None))
        await f

    def wait_for(self, id: str):
        self.bus.force_non_jd_thread()
        cv = threading.Condition()
        happened = False

        def poke(*args: object):
            nonlocal happened
            with cv:
                happened = True
                cv.notify()

        self.once(id, poke)
        with cv:
            while not happened:
                cv.wait()
