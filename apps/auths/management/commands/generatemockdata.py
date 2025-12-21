# Python modules
from datetime import datetime
from random import choice
from typing import Any

# Django modules
from django.core.management.base import BaseCommand

# Application modules
from apps.auths.models import CustomUser

class Command(BaseCommand):
    help = "Generate data for testing purposes"

    EMAIL_DOMAINS = (
        "example.com",
        "test.com",
        "sample.org",
        "demo.net",
        "mail.com",
    )

    SOME_WORDS = (
        "lorem",
        "ipsum",
        "dolor",
        "sit",
        "amet",
        "consectetur",
        "adipiscing",
        "elit",
        "sed",
        "do",
        "eiusmod",
        "tempor",
        "incididunt",
        "ut",
        "labore",
        "et",
        "dolore",
        "magna",
        "aliqua",
    )

    def _generate_users(self,accounts_count = 10) -> None:
        """
        Generates specified number of mock accounts in the database.
        """

        ACCOUNT_PASSWORD = "simplePass123"
        accounts_before : int = CustomUser.objects.count()
        for i in range(accounts_count):
            email : str = f"account{i + 1}@{choice(self.EMAIL_DOMAINS)}"
            full_name = choice(self.SOME_WORDS).capitalize() + ' ' + choice(self.SOME_WORDS).capitalize()
            role = choice([r.value for r in CustomUser.Roles])
            CustomUser.objects.create_user(
                email=email,
                full_name=full_name,
                password=ACCOUNT_PASSWORD,
                role=role
            )

        accounts_after : int = CustomUser.objects.count()

        self.stdout.write(
            self.style.SUCCESS(
                f"created {accounts_after - accounts_before} accounts."
            )
        )

    def handle(self, *args:tuple[Any, ...], **kwargs:dict[str, Any]) -> None:
        """
        Command entry point.
        """
        start_time :datetime = datetime.now()
        self._generate_users(accounts_count=100)
        self.stdout.write(
             "The whole process to generate data took: {} seconds".format(
                (datetime.now() - start_time).total_seconds()
            )
        )
