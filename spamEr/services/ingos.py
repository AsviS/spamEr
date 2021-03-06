from service import Service
from random import randint


class Ingos(Service):
    async def run(self):
        if self.phone_code == "7":
            await self.post(
                "https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",
                headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},
                json={
                    "Birthday": "1986-07-10T07:19:56.276+02:00",
                    "DocIssueDate": "2004-02-05T07:19:56.276+02:00",
                    "DocNumber": randint(500000, 999999),
                    "DocSeries": randint(5000, 9999),
                    "FirstName": self.russian_name,
                    "Gender": "M",
                    "LastName": self.russian_name,
                    "SecondName": self.russian_name,
                    "Phone": self.phone,
                    "Email": self.email,
                },
            )
