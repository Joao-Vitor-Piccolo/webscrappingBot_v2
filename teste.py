# from bot_do_Chat import Bot
# import api_data
# import datetime as dt
#
# room_id = 'MaiHL6MycT'
# gap = dt.timedelta(minutes=15)
#
#
# bot = Bot(headers=api_data.headers, cookies=api_data.cookies, params=api_data.params)
#
# print(bot.see_status())

import requests
import api_data as ad
from bot_do_Chat import Bot

bot = Bot(headers=ad.headers, cookies=ad.cookies, params=ad.params)

msg = 'oi'
id_pessoa = '3193fcb914af65a1f3af3a1638d7f75c'
id_saladeTeste = 'sjKMul2iCr'

print(bot.join_room(room_id=id_saladeTeste))

