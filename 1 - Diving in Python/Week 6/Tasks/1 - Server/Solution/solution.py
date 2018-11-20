import sys
import asyncio


data_storage = {}


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())


def process_data(data):
    command, payload = data.split(' ', 1)
    if command == 'put':
        splt = put(payload)
        return splt
    elif command == 'get':
        splt = get(payload)
        return splt
    else:
        return 'error\nwrong command\n\n'


def put(data):
    metric_name, metric_value, timestamp = data.split()
    if metric_name not in data_storage:
        data_storage[metric_name] = {}
    else:
        pass
    data_storage[metric_name].update({timestamp: metric_value})
    return 'ok\n\n'


def get(data):
    key = data.strip()
    if key == '*':
        response = 'ok\n'
        for key, value in data_storage.items():
            for v in sorted(value):
                response += '%s %s %s\n' % (key, value[v], v)
        response += '\n'
        return response
    else:
        values = data_storage.get(key)
        if values:
            response = 'ok\n'
            for current_value in sorted(values):
                response += '%s %s %s\n' % (key, values[current_value], current_value)
            response += '\n'
            return response
        else:
            return 'ok\n\n'