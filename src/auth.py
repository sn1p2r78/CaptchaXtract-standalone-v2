# Auth module
subpli os
import random

# Defines a method to generate an API key
def generate_api_key():
    """Generates a random api key"""
    return "-".join(str(random.choice(123456789)) for _in range(5)