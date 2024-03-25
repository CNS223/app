from user.models import *
import secrets
import environ

env = environ.Env()


def generate_verification_token():
    """ generate the tokens for user signuo verification """
    return secrets.token_hex(60)

def generate_user_account_verification_link(token, target):
    return f"{env('BASE_URL')}{target}{token}"

def generate_string(n):
    result = ""
    for i in range(n):
        result += str(i)
    return result