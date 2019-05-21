from concurrent.futures import ThreadPoolExecutor


class Pinger:
    def __init__(self, method='ping', target=None, max_workers=100):
        """
        initialize as a basic pinger type
        :param method: ping/tcp/udp
        :param target: target info object
        """
        if not self._check_param(method, target):
            raise ValueError("Invalid Ping Argument: {} => {}".format(str(target), str(target)))
        if not isinstance(max_workers, int):
            raise TypeError("Pinger max_worker not int: " + str(max_workers))
        if max_workers < 0:
            raise ValueError("Pinger max_worker negative value: " + str(max_workers))
        self.method = method
        self.target = target
        self.executor = ThreadPoolExecutor(max_workers)

    @staticmethod
    def _check_param(m, t):
        if m not in ['ping', 'tcp', 'udp']:
            return False
        if not t:
            return False
        return True

    @staticmethod
    def _do_ping(m, t):
        pass

    def ping(self, method=None, target=None, async_callback=None):
        """
        pass an alternative method and target for a temp ping task.
        The basic method and target is not affected.
        :param async_callback: def async_callback(future): # future.result(), future.method, future.target
        :return:
        """
        m = self.method
        t = self.target
        if method:
            m = method
        if target:
            t = target
        if not self._check_param(m, t):
            raise ValueError("Invalid Ping Argument: {} => {}".format(str(m), str(t)))
        # TODO: imp do_ping
        if async_callback:
            if not callable(async_callback):
                raise TypeError("Invalid Ping Callback")
            future = self.executor.submit(self._do_ping, m, t)
            future.method = m
            future.target = t
            future.add_done_callback(async_callback)
        else:
            self._do_ping(m, t)
