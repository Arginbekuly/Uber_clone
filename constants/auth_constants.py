# -------------------- ROLES -------------------- #

Roles = [
    {
        "role_code" : 'ADMIN',
    },
    {
        "role_code" : 'USER',
    },
    {
        "role_code" : 'DRIVER',
    }
]

default_role = 'USER'

ROLE_CHOICES = [(role['role_code'], role['role_code']) for role in Roles]
ROLES_LIST = [role['role_code'] for role in Roles]