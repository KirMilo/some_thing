import os

import aiohttp
import asyncio
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

dt_start: datetime
dt_end: datetime


async def find_all_elements(start_dt: datetime, end_dt: datetime, **kwargs):
    output = {"code": 200, "data": list()}
    divider = start_dt

    async with aiohttp.ClientSession() as session:

        while True:
            payload = {
                "user": os.getenv("USER"),
                "token": os.getenv("TOKEN"),
                "category_id": 7,
                "nedvigimost_type": "2, 3",
                "source": 4,
                "city": "Нижний Новгород",
                "date1": divider.strftime("%Y-%m-%d %H:%M:%S"),
                "date2": end_dt.strftime("%Y-%m-%d %H:%M:%S"),
                **kwargs,
            }

            async with session.get(
                    url="https://ads-api.ru/main/api",
                    params=payload,
            ) as resp:
                response = await resp.json()

                # status_code
                # print(f"status_code={resp.status}")

                if resp.status == 200:

                    # length
                    # print(f"length_tmp={len(response["data"])}")

                    if len(response["data"]) >= 1000:
                        divider += timedelta(days=1)
                        payload["date1"] = divider.strftime("%Y-%m-%d %H:%M:%S")

                    else:
                        output["data"] += response["data"]
                        # print(f"len_output={len(output)}")

                        if divider > start_dt:
                            end_dt = divider
                            payload["date2"] = end_dt.strftime("%Y-%m-%d %H:%M:%S")

                            divider = start_dt
                            payload["date1"] = divider.strftime("%Y-%m-%d %H:%M:%S")

                        else:
                            break

                    await asyncio.sleep(4)

                else:
                    print("gg", response)
                    return response

        print(f"length = {len(output["data"])}\n")
        return output


dt1 = datetime.strptime("2024-03-25 14:43:35", "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime("2024-04-10 14:43:35", "%Y-%m-%d %H:%M:%S")
asyncio.run(find_all_elements(start_dt=dt1, end_dt=dt2))
