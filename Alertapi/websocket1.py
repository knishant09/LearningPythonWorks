import asyncio
import websockets, json, ssl


async def test():
   # websockets.enableTrace(True)



    async with websockets.connect('wss://192.168.20.65:8443/pusher/alerts', extra_headers={'Authorization: Basic YWRtaW46Q3VtdWx1c0Ax'}) as ws:

        payload = { "function": "subscribe", "alertId": [443,444, 445, 446, 447, 448]}
        print(payload)
        await ws.send(payload)

        response = await ws.recv()
        print(response)






       # ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


asyncio.get_event_loop().run_until_complete(test())