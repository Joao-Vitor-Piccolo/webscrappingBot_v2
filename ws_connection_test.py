import asyncio
import requests
import random
import string
import api_data as ad
import json
import aiohttp
import time


def make_token():
    parte1 = ''.join(random.choices(string.ascii_lowercase, k=2))
    parte2 = ''.join(random.choices(string.digits, k=1))
    parte3 = ''.join(random.choices(string.ascii_lowercase, k=4))
    parte4 = ''.join(random.choices(string.digits, k=1))
    token = parte1 + parte2 + parte3 + parte4
    return token


def make_sid():
    token = make_token()
    print('printing token:', token)
    response = requests.get(f'https://drrr.com/conn/?version=4.1&EIO=4&transport=polling&t={token}', cookies=ad.cookies,
                            headers=ad.headers)
    dict_sid = dict(json.loads(response.text[1:]))
    sid_f = dict_sid['sid']
    print('printing sid: ', sid_f)
    print()
    return sid_f


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

sid = make_sid()


async def connect_to_websocket(sid_f):
    url = f'wss://drrr.com/conn/?version=4.1&EIO=4&transport=websocket&sid={sid_f}'

    async with aiohttp.ClientSession(headers=ad.headers, cookies=ad.cookies) as session:
        async with session.ws_connect(url) as ws:
            print("Conectado ao WebSocket!")
            await ws.send_str("2probe")
            print("[Enviado]: 2probe")

            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    print(f"[Recebido]: {msg.data}")

                    if msg.data == "3probe":
                        await ws.send_str("5")
                        print("[Enviado]: 5")
                    elif msg.data == "2":
                        await ws.send_str("3")
                        print("[Enviado]: 3")

                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    print("[Conexão encerrada]")
                    break

                elif msg.type == aiohttp.WSMsgType.ERROR:
                    print("[Erro no WebSocket]")
                    break


if __name__ == "__main__":
    asyncio.run(connect_to_websocket(sid))
