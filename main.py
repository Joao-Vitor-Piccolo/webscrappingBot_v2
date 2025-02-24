from bot_do_Chat import Bot
import datetime as dt
from time import sleep
from json import JSONDecodeError
import api_data as ap

room_id = 'cAoW4nXlFM'

if __name__ == '__main__':
    bot = Bot(cookies=ap.cookies, headers=ap.headers, params=ap.params)
    gap = dt.timedelta(minutes=15)

    try:
        bot.set_timelimit(bot=bot, gap=gap)
    except KeyError:
        bot.join_room(room_id)
        sleep(1)
        bot.set_timelimit(bot=bot, gap=gap)

    while True:
        sleep(2)
        try:
            if bot.see_status():
                try:
                    time_limit = bot.set_timelimit(bot=bot, gap=gap)
                    print(f'time_limit: {time_limit}')
                    if int(time_limit.replace(":", "")) <= int(dt.datetime.now().strftime("%H:%M").replace(":", "")):
                        print(f'the time is over the limit: {time_limit}')
                        bot.send_weeb_quote()
                        sleep(1)
                        time_limit = bot.set_timelimit(bot=bot, gap=gap)
                        print(f'New Time Limit: {time_limit}')
                except KeyError:
                    bot.join_room(room_id)
                except JSONDecodeError:
                    print("The response isn't a valid JSON")
            else:
                bot.join_room(room_id)
        except JSONDecodeError:
            print("The response isn't a valid JSON")
