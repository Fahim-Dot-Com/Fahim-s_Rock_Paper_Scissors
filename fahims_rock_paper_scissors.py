# fahims_rock_paper_scissors.py

import time

def seed_custom():
    # Seed based on current time (for randomness)
    return int(time.time() * 1000000) % 1000003

def custom_choice(options):
    index = seed_custom() % len(options)
    return options[index]
