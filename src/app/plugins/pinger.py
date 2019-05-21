from concurrent.futures import ThreadPoolExecutor
from app.servers.models import Server


class Pinger:
    def __init__(self, serverinfo=None, max_workers=100):
        """
        initialize as a basic pinger type
        """
        if not self._check_param(serverinfo):
            raise ValueError("Invalid Ping Argument: " + str(serverinfo))
        if not isinstance(max_workers, int):
            raise TypeError("Pinger max_worker not int: " + str(max_workers))
        if max_workers < 0:
            raise ValueError("Pinger max_worker negative value: " + str(max_workers))
        self.executor = ThreadPoolExecutor(max_workers)

    @staticmethod
    def _check_param(serviceinfo):
        if not serviceinfo:
            return False
        if not isinstance(serviceinfo, Server):
            return False
        if serviceinfo.ping_method not in ['ping', 'tcp', 'udp']:
            return False
        return True

    @staticmethod
    def _do_ping(serviceinfo):
        # TODO: imp _do_ping
        pass

    def ping(self, serviceinfo=None, async_callback=None):
        """
        pass an alternative method and target for a temp ping task.
        The basic method and target is not affected.
        :param async_callback: def async_callback(future): # future.result(), future.method, future.target
        :return:
        """
        if not self._check_param(serviceinfo):
            raise ValueError("Invalid Ping Argument: " + str(serviceinfo))
        if async_callback:
            if not callable(async_callback):
                raise TypeError("Invalid Ping Callback")
            future = self.executor.submit(self._do_ping, serviceinfo)
            future.serviceinfo = serviceinfo
            future.add_done_callback(async_callback)
        else:
            self._do_ping(serviceinfo)
