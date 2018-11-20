import socket
import time


class ClientError:
    pass


class Client:
    def __init__(self, host, port, timeout):
        self.sock = socket.create_connection((host, port), timeout=timeout)

    def put(self, key, value, timestamp=None):
        send_time = timestamp
        if not send_time:
            send_time = int(time.time())

        send_string = "put " + key + " " + str(value) + " " + str(send_time) + "\n"
        self.sock.sendall(send_string.encode("utf8"))
        raw_data = self.sock.recv(1024).decode("utf8")
#        print(raw_data) #debug
#        raw_data = 'ok\n\n' #debug

        if raw_data == 'error\nwrong command\n\n':
            raise ClientError
        if not raw_data == 'ok\n\n':
#            print("WTF")  #debug
            raise ClientError

    def get(self, key):
        self.sock.sendall(("get " + key + "\n").encode("utf8"))
        raw_data = self.sock.recv(1024)
        raw_data = raw_data.decode("utf8")
#        raw_data = 'ok\n\n'  #debug
        if raw_data == 'ok\n\n':
            return {}
        elif not raw_data[:2] == 'ok':
#            print("NOT STARTS WITH OK")  #debug
            raise ClientError
        elif not raw_data[-2:] == '\n\n':
#            print("NOT FINISHES WITH LFLF")  #debug
            raise ClientError
        else:
            data = raw_data.split('\n')[1:-2]

            ans = dict()
            for current_data in data:
                data_split = current_data.split(' ')

                key = data_split[0]
                metric = float(data_split[1])
                timestamp = int(data_split[2])

                if key in ans.keys():
                    ans[key].append((timestamp, metric))
                else:
                    ans[key] = [(timestamp, metric)]

            return ans


if __name__ == '__main__':
    test_server = False

    if test_server:
        client = Client("127.0.0.1", 10001, timeout=15)

        client.put("palm.cpu", 0.5, timestamp=1150864247)
        client.put("palm.cpu", 2.0, timestamp=1150864248)
        client.put("palm.cpu", 0.5, timestamp=1150864248)

        client.put("eardrum.cpu", 3, timestamp=1150864250)
        client.put("eardrum.cpu", 4, timestamp=1150864251)
        client.put("eardrum.memory", 4200000)
