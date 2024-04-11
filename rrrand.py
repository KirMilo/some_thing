# # def some(*args, **kwargs):
# #     output = {"ggg": "aaaa", "bcd": "111", **kwargs}
# #     print(output)
# #
# #
# # some(a=50, b="abcd")
# from datetime import datetime, timedelta
#
# # abc = {1, 2, 3}
# #
# # abc = abc.union([3, 5, 6])
# #
# # print(abc)
#
# dt = datetime.strptime("2024-04-03 14:43:35", "%Y-%m-%d %H:%M:%S")
#
# print(dt)
# dt2 = dt
#
# dt += timedelta(days=1)
# print(dt == dt2)
#
# print(dt)
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

dt1 = datetime.strptime("2024-04-10 10:43:35", "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime("2024-04-10 12:43:35", "%Y-%m-%d %H:%M:%S")

payload = {
    "user": os.getenv("USER"),
    "token": os.getenv("TOKEN"),
    "category_id": 7,
    "nedvigimost_type": "2, 3",
    "source": 4,
    "city": "Нижний Новгород",
    "date1": dt1.strftime("%Y-%m-%d %H:%M:%S"),
    "date2": dt2.strftime("%Y-%m-%d %H:%M:%S"),
}

response = requests.get(url="https://ads-api.ru/main/api", params=payload)
data = response.json()
print(len(data["data"]))
