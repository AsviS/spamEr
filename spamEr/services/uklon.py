from service import Service


class Uklon(Service):
    async def run(self):
        await self.post(
            "https://www.uklon.com.ua/api/v1/account/code/send",
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": self.formatted_phone},
        )
