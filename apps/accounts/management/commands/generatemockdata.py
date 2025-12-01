from django.contrib.auth.hashers import make_password
from apps.accounts.models import Account
from random import choice
from constants.auth_constants import ROLES_LIST
from django.core.management.base import BaseCommand
from typing import Any
from datetime import datetime

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
    
    def _generate_accounts(self,accounts_count = 10) -> None:
        """
        Generates specified number of mock accounts in the database.
        """
        
        ACCOUNT_PASSWORD = make_password(password = "simplePass123")
        created_users : list[Account]= []
        accounts_before : int = Account.objects.count()
        for i in range(accounts_count):
            username : str = f"account {i + 1}"
            email : str = f"account{i + 1}@{choice(self.EMAIL_DOMAINS)}"
            created_users.append(
                Account(
                    username = username,
                    email = email,
                    password = ACCOUNT_PASSWORD,
                    first_name = choice(self.SOME_WORDS).capitalize(),
                    last_name = choice(self.SOME_WORDS).capitalize(),
                    role = choice(ROLES_LIST),
                )
            )
        Account.objects.bulk_create(created_users, ignore_conflicts = True)
        accounts_after : int = Account.objects.count()
        
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
        self._generate_accounts(accounts_count=20)
        self.stdout.write(
             "The whole process to generate data took: {} seconds".format(
                (datetime.now() - start_time).total_seconds()
            )
        ) 