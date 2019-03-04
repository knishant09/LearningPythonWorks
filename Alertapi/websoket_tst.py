import websocket, json, ssl



class WebSocketClientError(Exception):
    pass
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):

        for i in range(100):

            time.sleep(5)

            ws.send(json.dumps([json.dumps({"function":"subscribe", "alertId":[443,444, 445, 446, 447, 448]})]))
            print(ws.recv())
            result = ws.recv()
            print('Result: {}'.format(result))
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)

    try:
        ws = websocket.WebSocketApp("wss://192.168.20.65:8443/pusher/alerts",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              header =  {'Authorization: Basic YWRtaW46Q3VtdWx1c0Ax'}

                                )
    except Exception as e:
            raise WebSocketClientError("Error While Connecting : %s" % str(e))

    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


