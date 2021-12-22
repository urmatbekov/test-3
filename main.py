import aiohttp
import asyncio

url = "https://api.openweathermap.org/data/2.5/weather?id={}&lang=ru&appid=7821591e8b20bbefdb453db278b342cd"


async def main(city):
    async with aiohttp.ClientSession() as session:
        async with session.get(url.format(city["id"])) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            file = open('{}.json'.format(city["name"]), 'w')
            file.write(html)
            file.close()


city_list = [
    {
        "id": "1528675",
        "name": "Bishkek"
    }, {
        "id": "524901",
        "name": "Moskva"
    }, {
        "id": "1527534",
        "name": "Osh"
    },
]

loop = asyncio.get_event_loop()
for city in city_list:
    loop.run_until_complete(main(city))

